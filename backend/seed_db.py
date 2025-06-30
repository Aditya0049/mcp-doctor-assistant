# seed_db.py
import asyncio
from app.db import setup_db

asyncio.run(setup_db())
