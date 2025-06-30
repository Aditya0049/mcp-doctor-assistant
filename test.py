import asyncio
import asyncpg

async def test():
    conn = await asyncpg.connect("postgresql://postgres:PB6TJEg52gg.FR2@db.mngdchcycmeaetmvmmlu.supabase.co:5432/postgres?sslmode=require")
    print("✅ Connected!")
    await conn.close()

asyncio.run(test())
