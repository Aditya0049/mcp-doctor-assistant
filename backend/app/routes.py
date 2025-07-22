from fastapi import APIRouter
from pydantic import BaseModel
from app.agent import run_agent

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/agent/prompt")
async def handle_prompt(req: PromptRequest):
    result = await run_agent(req.prompt)
    return {"response": result}
