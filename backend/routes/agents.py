from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from backend.agents import (
    LearningAgent,
    AIUsageAgent,
    ActivityAgent,
    GameAgent,
    HabitCoachAgent,
    GoalPlannerAgent
)

router = APIRouter(prefix="/api/agents", tags=["agents"])

# In-memory agent storage
agents_db = {}

class StudySessionLog(BaseModel):
    subject: str
    duration_minutes: int
    quality_score: float

class AIInteractionLog(BaseModel):
    tool: str
    action: str
    reflection: Optional[str] = ""

class ActivityLog(BaseModel):
    activity_type: str
    duration_minutes: int

class QuizScore(BaseModel):
    subject: str
    score: float

class DailyMetrics(BaseModel):
    sleep_hours: float
    study_hours: float
    focus_time: int
    reading_minutes: int

def get_or_create_agents(student_id: str):
    """Get or create agent instances for a student."""
    if student_id not in agents_db:
        agents_db[student_id] = {
            "learning": LearningAgent(student_id),
            "ai_usage": AIUsageAgent(student_id),
            "activity": ActivityAgent(student_id),
            "game": GameAgent(student_id),
            "habit": HabitCoachAgent(student_id),
            "goals": GoalPlannerAgent(student_id)
        }
    return agents_db[student_id]

# ==================== LEARNING AGENT ====================
@router.post("/{student_id}/learning/log-session")
async def log_study_session(student_id: str, session: StudySessionLog):
    """
    Log a study session for learning agent.
    """
    agents = get_or_create_agents(student_id)
    agents["learning"].log_study_session(
        session.subject,
        session.duration_minutes,
        session.quality_score
    )
    return {
        "status": "logged",
        "message": f"Study session logged: {session.subject}"
    }

@router.post("/{student_id}/learning/log-quiz")
async def log_quiz_score(student_id: str, quiz: QuizScore):
    """
    Log a quiz score.
    """
    agents = get_or_create_agents(student_id)
    agents["learning"].log_quiz_score(quiz.subject, quiz.score)
    return {
        "status": "logged",
        "score": quiz.score,
        "subject": quiz.subject
    }

@router.get("/{student_id}/learning/analytics")
async def get_learning_analytics(student_id: str):
    """
    Get learning analytics.
    """
    agents = get_or_create_agents(student_id)
    return agents["learning"].get_study_analytics()

@router.get("/{student_id}/learning/recommendation")
async def get_learning_recommendation(student_id: str):
    """
    Get personalized learning path recommendation.
    """
    agents = get_or_create_agents(student_id)
    return agents["learning"].get_learning_path_recommendation()

# ==================== AI USAGE AGENT ====================
@router.post("/{student_id}/ai-usage/log-interaction")
async def log_ai_interaction(student_id: str, interaction: AIInteractionLog):
    """
    Log an AI tool interaction.
    """
    agents = get_or_create_agents(student_id)
    agents["ai_usage"].log_ai_interaction(
        interaction.tool,
        interaction.action,
        interaction.reflection
    )
    return {
        "status": "logged",
        "tool": interaction.tool,
        "message": "AI interaction tracked for responsible usage analysis"
    }

@router.get("/{student_id}/ai-usage/report")
async def get_ai_usage_report(student_id: str):
    """
    Get AI usage report with score and classification.
    """
    agents = get_or_create_agents(student_id)
    return agents["ai_usage"].get_ai_usage_report()

@router.get("/{student_id}/ai-usage/recommendation")
async def get_ai_usage_recommendation(student_id: str):
    """
    Get AI usage improvement recommendation.
    """
    agents = get_or_create_agents(student_id)
    return {"recommendation": agents["ai_usage"].get_recommendation()}

# ==================== ACTIVITY AGENT ====================
@router.post("/{student_id}/activity/log")
async def log_activity(student_id: str, activity: ActivityLog):
    """
    Log physical activity.
    """
    agents = get_or_create_agents(student_id)
    agents["activity"].log_activity(activity.activity_type, activity.duration_minutes)
    return {
        "status": "logged",
        "activity": activity.activity_type,
        "duration": activity.duration_minutes
    }

@router.get("/{student_id}/activity/break-recommendation/{study_duration_minutes}")
async def get_break_recommendation(student_id: str, study_duration_minutes: int):
    """
    Get break recommendation based on study duration.
    """
    agents = get_or_create_agents(student_id)
    return agents["activity"].get_break_recommendation(study_duration_minutes)

@router.get("/{student_id}/activity/daily-goal")
async def get_activity_goal(student_id: str):
    """
    Get daily activity goals.
    """
    agents = get_or_create_agents(student_id)
    return agents["activity"].get_daily_activity_goal()

@router.get("/{student_id}/activity/analytics")
async def get_activity_analytics(student_id: str):
    """
    Get activity analytics.
    """
    agents = get_or_create_agents(student_id)
    return agents["activity"].get_activity_analytics()

# ==================== GAME AGENT ====================
@router.post("/{student_id}/game/create-mission")
async def create_mission(student_id: str, subject: str, difficulty: str = "medium"):
    """
    Create a new mission for a subject.
    """
    agents = get_or_create_agents(student_id)
    mission = agents["game"].create_daily_mission(subject, difficulty)
    return mission

@router.post("/{student_id}/game/complete-mission/{mission_id}")
async def complete_mission(student_id: str, mission_id: str):
    """
    Complete a mission and earn XP.
    """
    agents = get_or_create_agents(student_id)
    result = agents["game"].complete_mission(mission_id)
    return result

@router.get("/{student_id}/game/stats")
async def get_game_stats(student_id: str):
    """
    Get game statistics (level, XP, badges).
    """
    agents = get_or_create_agents(student_id)
    return agents["game"].get_game_stats()

@router.get("/{student_id}/game/mission-board")
async def get_mission_board(student_id: str):
    """
    Get mission board view.
    """
    agents = get_or_create_agents(student_id)
    return agents["game"].get_mission_board()

# ==================== HABIT COACH AGENT ====================
@router.post("/{student_id}/habits/log-daily")
async def log_daily_metrics(student_id: str, metrics: DailyMetrics):
    """
    Log daily metrics (sleep, study, focus, reading).
    """
    agents = get_or_create_agents(student_id)
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d")
    agents["habit"].log_daily_metrics(date, metrics.dict())
    return {
        "status": "logged",
        "date": date,
        "message": "Daily metrics recorded"
    }

@router.get("/{student_id}/habits/feedback")
async def get_habit_feedback(student_id: str):
    """
    Get daily habit feedback and recommendations.
    """
    agents = get_or_create_agents(student_id)
    return agents["habit"].get_daily_feedback()

@router.get("/{student_id}/habits/analytics")
async def get_habit_analytics(student_id: str):
    """
    Get habit tracking analytics.
    """
    agents = get_or_create_agents(student_id)
    return agents["habit"].get_habit_analytics()

@router.get("/{student_id}/habits/weekly-summary")
async def get_weekly_summary(student_id: str):
    """
    Get weekly habit summary.
    """
    agents = get_or_create_agents(student_id)
    return agents["habit"].get_weekly_summary()

# ==================== GOAL PLANNER AGENT ====================
@router.post("/{student_id}/goals/create")
async def create_goal(student_id: str, goal_text: str, target_score: float = None, subject: str = None, timeline_days: int = 30):
    """
    Create a goal for the student.
    """
    agents = get_or_create_agents(student_id)
    goal = agents["goals"].create_goal(goal_text, target_score, subject, timeline_days)
    return goal

@router.post("/{student_id}/goals/{goal_id}/update-progress")
async def update_goal_progress(student_id: str, goal_id: str, current_score: float):
    """
    Update goal progress.
    """
    agents = get_or_create_agents(student_id)
    agents["goals"].update_progress(goal_id, current_score)
    return {"status": "updated", "goal_id": goal_id, "progress": current_score}

@router.get("/{student_id}/goals/dashboard")
async def get_goal_dashboard(student_id: str):
    """
    Get goal dashboard.
    """
    agents = get_or_create_agents(student_id)
    return agents["goals"].get_goal_dashboard()

@router.get("/{student_id}/goals/weekly-review")
async def get_weekly_review(student_id: str):
    """
    Get weekly review for goals.
    """
    agents = get_or_create_agents(student_id)
    return agents["goals"].get_weekly_review()

# ==================== MULTI-AGENT DASHBOARD ====================
@router.get("/{student_id}/dashboard")
async def get_complete_dashboard(student_id: str):
    """
    Get complete multi-agent dashboard showing all agent insights.
    """
    agents = get_or_create_agents(student_id)
    
    return {
        "student_id": student_id,
        "learning": agents["learning"].get_study_analytics(),
        "ai_usage": agents["ai_usage"].get_ai_usage_report(),
        "activity": agents["activity"].get_activity_analytics(),
        "game": agents["game"].get_game_stats(),
        "habits": agents["habit"].get_habit_analytics(),
        "goals": agents["goals"].get_goal_dashboard(),
        "timestamp": datetime.now().isoformat()
    }
