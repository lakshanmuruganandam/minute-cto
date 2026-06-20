from fastapi import APIRouter
from src.models.architecture import Requirements, ArchitectureOutput
from src.services.agent import CTOAgent

api_router = APIRouter()
agent = CTOAgent()

@api_router.post("/architecture/generate", response_model=dict)
async def generate_architecture(req: Requirements):
    arch = await agent.generate_architecture(req)
    return {
        "status": "success", 
        "architecture": arch.model_dump()
    }
