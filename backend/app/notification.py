# app/notification.py

# 🔔 MOCK notification sender for doctor summary
async def send_doctor_notification(doctor: str, message: str) -> str:
    print(f"📲 Notification sent to {doctor} with message:\n{message}")
    return "✅ Notification sent (mocked)"
