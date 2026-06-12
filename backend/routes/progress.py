from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/api/progress", tags=["progress"])

# In-memory progress tracking
progress_db = {}

class ProgressUpdate(BaseModel):
    category: str  # learning, ai_usage, activity, habits, goals
    value: float
    description: Optional[str] = ""

@router.post("/{student_id}")
async def record_progress(student_id: str, progress: ProgressUpdate):
    """
    Record student progress.
    """
    if student_id not in progress_db:
        progress_db[student_id] = []
    
    record = {
        "category": progress.category,
        "value": progress.value,
        "description": progress.description,
        "timestamp": datetime.now().isoformat()
    }
    
    progress_db[student_id].append(record)
    
    return {
        "status": "recorded",
        "progress": record,
        "total_records": len(progress_db[student_id])
    }

@router.get("/{student_id}")
async def get_progress(student_id: str):
    """
    Get student's progress history.
    """
    if student_id not in progress_db:
        return {"student_id": student_id, "progress": [], "total": 0}
    
    return {
        "student_id": student_id,
        "progress": progress_db[student_id],
        "total": len(progress_db[student_id])
    }

@router.get("/{student_id}/category/{category}")
async def get_progress_by_category(student_id: str, category: str):
    """
    Get progress for a specific category.
    """
    if student_id not in progress_db:
        return {"category": category, "progress": [], "total": 0}
    
    category_progress = [p for p in progress_db[student_id] if p["category"].lower() == category.lower()]
    
    return {
        "student_id": student_id,
        "category": category,
        "progress": category_progress,
        "total": len(category_progress)
    }

@router.get("/{student_id}/summary")
async def get_progress_summary(student_id: str):
    """
    Get summary of progress across all categories.
    """
    if student_id not in progress_db:
        return {
            "student_id": student_id,
            "summary": {
                "learning": 0,
                "ai_usage": 0,
                "activity": 0,
                "habits": 0,
                "goals": 0
            },
            "total_progress_points": 0
        }
    
    progress_list = progress_db[student_id]
    summary = {
        "learning": 0,
        "ai_usage": 0,
        "activity": 0,
        "habits": 0,
        "goals": 0
    }
    
    for p in progress_list:
        category = p["category"].lower()
        if category in summary:
            summary[category] += p["value"]
    
    return {
        "student_id": student_id,
        "summary": summary,
        "total_progress_points": sum(summary.values())
    }
