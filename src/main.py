
from fastapi import FastAPI
from src.api.router import api_router

app = FastAPI(
    title="Minute CTO",
    description="Autonomous Agent for Instant Tech Stack Architecture",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Minute CTO is ready to architect your startup."}
