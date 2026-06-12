from fastapi import APIRouter, HTTPException
from typing import Optional
import uuid
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/api/students", tags=["students"])

# In-memory storage (replace with database in production)
students_db = {}

class StudentCreate(BaseModel):
    name: str
    email: str

class StudentResponse(BaseModel):
    student_id: str
    name: str
    email: str
    character_class: str
    level: int
    xp: int
    created_at: str

@router.post("/", response_model=StudentResponse)
async def create_student(student_data: StudentCreate):
    """
    Create a new student profile.
    """
    student_id = str(uuid.uuid4())
    student = {
        "student_id": student_id,
        "name": student_data.name,
        "email": student_data.email,
        "character_class": "Explorer",
        "level": 1,
        "xp": 0,
        "created_at": datetime.now().isoformat()
    }
    students_db[student_id] = student
    return student

@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: str):
    """
    Get student profile by ID.
    """
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]

@router.get("/")
async def list_students():
    """
    List all students.
    """
    return {"students": list(students_db.values()), "count": len(students_db)}

@router.put("/{student_id}")
async def update_student(student_id: str, student_data: StudentCreate):
    """
    Update student profile.
    """
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    students_db[student_id].update({
        "name": student_data.name,
        "email": student_data.email
    })
    return students_db[student_id]
