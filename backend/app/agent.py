import os
from typing import Optional
from datetime import datetime, timedelta

from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory

from langchain.agents import AgentExecutor
from langchain.agents.openai_functions_agent.base import create_openai_functions_agent
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder

from app.db import get_available_appointments
from app.calendar import book_appointment
from app.email import send_email_confirmation
from app.notification import send_doctor_notification

# --- Input Schemas ---
class AvailabilityInput(BaseModel):
    doctor_name: str
    date: str
    time: Optional[str] = None

class AppointmentInput(BaseModel):
    doctor_name: str
    date: str
    time: str
    user_email: str

class EmailInput(BaseModel):
    recipient: str
    subject: str
    content: str

class NotificationInput(BaseModel):
    doctor_name: str
    message: str

# --- Helper ---
def normalize_date(date_str: str) -> str:
    if date_str.lower() == "tomorrow":
        return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    return date_str

# --- Tools ---
@tool("CheckDoctorAvailability", args_schema=AvailabilityInput)
def check_doctor_availability(doctor_name: str, date: str, time: Optional[str] = None):
    """Check if a doctor is available at a specific date and time."""
    try:
        normalized_date = normalize_date(date)
        return get_available_appointments(doctor_name, normalized_date, time)
    except Exception as e:
        return f"❌ Availability Tool Error: {str(e)}"

@tool("BookAppointment", args_schema=AppointmentInput)
def book_appointment_tool(doctor_name: str, date: str, time: str, user_email: str):
    """Book an appointment for a user with a specific doctor."""
    try:
        normalized_date = normalize_date(date)
        return book_appointment(doctor_name, normalized_date, time, user_email)
    except Exception as e:
        return f"❌ Booking Tool Error: {str(e)}"

@tool("SendEmail", args_schema=EmailInput)
def send_email_tool(recipient: str, subject: str, content: str):
    """Send an email to a user."""
    try:
        return send_email_confirmation(recipient, subject, content)
    except Exception as e:
        return f"❌ Email Tool Error: {str(e)}"

@tool("SendDoctorNotification", args_schema=NotificationInput)
def send_doctor_notification_tool(doctor_name: str, message: str):
    """Send a notification to the doctor."""
    try:
        return send_doctor_notification(doctor_name, message)
    except Exception as e:
        return f"❌ Notification Tool Error: {str(e)}"

# --- LLM & Memory ---
llm = ChatOllama(model="mistral")  # You can switch to OpenAI if needed
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# --- Tools ---
tools = [
    check_doctor_availability,
    book_appointment_tool,
    send_email_tool,
    send_doctor_notification_tool
]

# --- Prompt ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful healthcare assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# --- Agent ---
agent_executor = AgentExecutor(
    agent=create_openai_functions_agent(llm, tools, prompt),
    tools=tools,
    memory=memory,
    verbose=True
)

# --- Main Runner ---
async def run_agent(user_prompt: str) -> str:
    print(f"\n📥 Prompt received: {user_prompt}")
    try:
        result = await agent_executor.ainvoke({"input": user_prompt})
        return result["output"]
    except Exception as e:
        print(f"❌ Agent Error: {e}")
        return "Sorry, something broke."
