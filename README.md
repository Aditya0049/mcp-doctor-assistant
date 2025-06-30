# 🧠 Smart Doctor Assistant (Agentic AI)

This is a full-stack demo built as part of the FSE Intern Assignment using:

- FastAPI + LangChain + React
- Agentic design with MCP tools (availability, booking, email, report)

## 🚀 Features

- Prompt-based appointment booking via AI
- Summary report generation for doctors
- Conversation memory (multi-turn)

## 🔧 Tech Stack

- Backend: FastAPI, LangChain, MCP-style toolchain
- Frontend: React + Tailwind CSS
- DB: Supabase PostgreSQL (mocked)

## 📦 Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# .env file
cp .env.example .env
```

## 🖥️ Run
```bash
uvicorn app.main:app --reload
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

## ✨ Sample Prompts

- Book appointment with Dr. Ahuja tomorrow
- How many patients visited yesterday?

---

## 📸 Screenshots

- ![booking.png](demo-screenshots/booking.png)
- ![summary.png](demo-screenshots/summary.png)


## 👤 Bonus

- Role-based login (optional)
- Prompt history (optional)
- LLM auto rescheduling (TODO)

---
MIT License.
