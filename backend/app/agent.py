# app/agent.py
import os
import asyncio
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool

from app.db import get_available_appointments, get_doctor_summary
from app.calendar import book_appointment
from app.email import send_email_confirmation
from app.notification import send_doctor_notification

# 🔁 Wrap async functions to run as sync
def sync_wrapper(async_func):
    def wrapper(*args, **kwargs):
        return asyncio.run(async_func(*args, **kwargs))
    return wrapper

llm = ChatOllama(model="mistral")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [
    Tool(
        name="CheckDoctorAvailability",
        func=sync_wrapper(get_available_appointments),
        description="Check the doctor's availability"
    ),
    Tool(
        name="BookAppointment",
        func=sync_wrapper(book_appointment),
        description="Book a doctor's appointment"
    ),
    Tool(
        name="SendEmail",
        func=sync_wrapper(send_email_confirmation),
        description="Send a confirmation email to the patient"
    ),
    Tool(
        name="SendDoctorNotification",
        func=sync_wrapper(send_doctor_notification),
        description="Send a summary notification to the doctor"
    ),
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    handle_parsing_errors=True
)

# 🚀 Main function for agent response
async def run_agent(user_prompt: str) -> str:
    print(f"📥 Prompt received: {user_prompt}")
    try:
        response = await agent.arun(user_prompt)
        print(f"✅ Agent Response: {response}")
        return response
    except Exception as e:
        print(f"❌ Agent error: {e}")
        return "🤖 Sorry, I couldn't understand. Try asking to book, check availability, or get summary."
