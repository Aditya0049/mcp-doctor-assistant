from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.agent import run_agent

router = APIRouter()

class PromptInput(BaseModel):
    prompt: str

@router.post("/agent/prompt")
async def agent_prompt(prompt: dict):
    user_input = prompt.get("prompt", "")
    print(f"📥 Prompt received: {user_input}")
    try:
        response = await run_agent(user_input)
        print(f"✅ Agent response: {response}")
        return {"response": response}
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {"response": "Sorry, something went wrong."}
