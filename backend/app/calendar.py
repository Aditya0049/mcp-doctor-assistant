def book_appointment(doctor_name: str, date: str, time: str, user_email: str) -> str:
    print(f"📅 Booking appointment for {doctor_name} on {date} at {time} for {user_email}")
    # Mock confirmation
    return f"Appointment booked with {doctor_name} on {date} at {time} for {user_email}"