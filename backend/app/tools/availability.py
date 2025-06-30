from app.db import get_available_appointments

async def check_appointment(_: str):
    rows = await get_available_appointments("Dr. Ahuja")
    if rows:
        slot = rows[0]
        return f"✅ Available on {slot['date']} at {slot['time_slot']}"
    return "❌ No available slots."

