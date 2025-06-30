# app/email.py

# 🔧 MOCK email sender function
async def send_email_confirmation(to_email: str, subject: str, body: str) -> str:
    print(f"📧 Email sent to {to_email} with subject '{subject}' and body:\n{body}")
    return "✅ Email sent (mocked)"
