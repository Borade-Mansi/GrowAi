from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter(prefix="/api/missions", tags=["missions"])

# Sample missions data
SAMPLE_MISSIONS = [
    {
        "id": "mission_1",
        "title": "Solve 5 Algebra Problems",
        "subject": "Math",
        "xp_reward": 100,
        "difficulty": "medium",
        "description": "Master basic algebra by solving 5 problems",
        "tasks": [
            "Solve linear equations",
            "Practice quadratic equations",
            "Test your understanding with a quiz"
        ]
    },
    {
        "id": "mission_2",
        "title": "Read for 15 Minutes",
        "subject": "Reading",
        "xp_reward": 75,
        "difficulty": "easy",
        "description": "Build your reading habit",
        "tasks": ["Read any educational material", "Reflect on what you learned"]
    },
    {
        "id": "mission_3",
        "title": "Advanced Calculus Challenge",
        "subject": "Math",
        "xp_reward": 200,
        "difficulty": "hard",
        "description": "For advanced learners - master derivatives",
        "tasks": [
            "Learn derivative rules",
            "Solve 10 derivative problems",
            "Complete challenge quiz"
        ]
    },
    {
        "id": "mission_4",
        "title": "Science Experiment Simulation",
        "subject": "Science",
        "xp_reward": 150,
        "difficulty": "medium",
        "description": "Complete an interactive science experiment",
        "tasks": ["Run simulation", "Analyze results", "Write observations"]
    },
    {
        "id": "mission_5",
        "title": "Writing Challenge",
        "subject": "English",
        "xp_reward": 125,
        "difficulty": "medium",
        "description": "Improve your writing skills",
        "tasks": ["Brainstorm topic", "Write essay draft", "Self-review"]
    }
]

@router.get("/")
async def get_all_missions():
    """
    Get all available missions.
    """
    return {"missions": SAMPLE_MISSIONS, "total": len(SAMPLE_MISSIONS)}

@router.get("/{mission_id}")
async def get_mission(mission_id: str):
    """
    Get a specific mission.
    """
    for mission in SAMPLE_MISSIONS:
        if mission["id"] == mission_id:
            return mission
    return {"error": "Mission not found"}

@router.get("/by-subject/{subject}")
async def get_missions_by_subject(subject: str):
    """
    Get missions for a specific subject.
    """
    subject_missions = [m for m in SAMPLE_MISSIONS if m["subject"].lower() == subject.lower()]
    return {"subject": subject, "missions": subject_missions, "count": len(subject_missions)}

@router.get("/by-difficulty/{difficulty}")
async def get_missions_by_difficulty(difficulty: str):
    """
    Get missions by difficulty level.
    """
    diff_missions = [m for m in SAMPLE_MISSIONS if m["difficulty"].lower() == difficulty.lower()]
    return {"difficulty": difficulty, "missions": diff_missions, "count": len(diff_missions)}
