def get_available_appointments(doctor_name: str, date: str, time: str = None) -> dict:
    print(f"🔍 get_available_appointments received: doctor_name='{doctor_name}' date='{date}' time='{time}'")
    # Mocked response: Doctor is available only at 10 AM
    if time:
        return {"available": time == "10 AM", "doctor": doctor_name, "date": date, "time": time}
    else:
        return {"available": True, "doctor": doctor_name, "date": date, "time": None}
