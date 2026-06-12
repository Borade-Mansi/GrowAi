from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from backend.routes import students_router, agents_router, missions_router, progress_router

load_dotenv()

app = FastAPI(
    title="GrowAi",
    description="Personal Growth Agent Platform - Agents League Hackathon 2026",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(students_router)
app.include_router(agents_router)
app.include_router(missions_router)
app.include_router(progress_router)

# Health check
@app.get("/")
async def root():
    return {
        "status": "healthy",
        "service": "GrowAi",
        "message": "Personal Growth Agent Platform is running",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "students": "/api/students",
            "agents": "/api/agents",
            "missions": "/api/missions",
            "progress": "/api/progress"
        }
    }

# Health endpoint
@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": "2026-06-12"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
