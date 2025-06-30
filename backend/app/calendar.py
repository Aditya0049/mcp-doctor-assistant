# app/calendar.py

import datetime

# 🔧 MOCK calendar booking tool
async def book_appointment(doctor: str, patient: str, time: str) -> str:
    # In actual implementation, you'd call Google Calendar API here
    return f"📅 Appointment with {doctor} for {patient} at {time} has been booked (mocked)."
