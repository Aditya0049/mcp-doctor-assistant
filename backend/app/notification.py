def send_doctor_notification(doctor_name: str, message: str) -> str:
    print(f"📨 Notifying Dr. {doctor_name} | Message: {message}")
    return f"Doctor {doctor_name} notified with message: {message}"