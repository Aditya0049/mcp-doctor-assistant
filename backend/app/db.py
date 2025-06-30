# app/db.py
import aiosqlite

DB_PATH = "app/data.db"

async def get_available_appointments(doctor: str) -> str:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT time FROM appointments WHERE doctor=? AND available=1",
            (doctor,)
        )
        rows = await cursor.fetchall()
        times = [row[0] for row in rows]
        return f"Available times for {doctor}: {', '.join(times)}" if times else f"No available slots for {doctor}."

async def get_doctor_summary(doctor: str = "Dr. Ahuja") -> str:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT COUNT(*) FROM appointments WHERE doctor=?", (doctor,)
        )
        count = (await cursor.fetchone())[0]
        return f"{doctor} has {count} total appointments."

async def setup_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doctor TEXT,
                time TEXT,
                available INTEGER
            )
        """)
        await db.execute("DELETE FROM appointments")
        appointments = [
            ("Dr. Ahuja", "2025-06-30 10:00", 1),
            ("Dr. Ahuja", "2025-06-30 11:00", 1),
            ("Dr. Ahuja", "2025-06-30 15:00", 0),
        ]
        await db.executemany(
            "INSERT INTO appointments (doctor, time, available) VALUES (?, ?, ?)",
            appointments
        )
        await db.commit()
