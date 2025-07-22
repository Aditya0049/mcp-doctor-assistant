from pydantic import BaseModel
from typing import Optional

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
