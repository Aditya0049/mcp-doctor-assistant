def send_email_confirmation(recipient: str, subject: str, content: str) -> str:
    print(f"📧 Sending email to {recipient} | Subject: {subject} | Content: {content}")
    return f"Email sent to {recipient} with subject '{subject}'"