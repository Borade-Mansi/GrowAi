"""Demo data generator for testing GrowAi."""

import random
from datetime import datetime, timedelta

def generate_demo_student():
    """Generate a demo student profile."""
    return {
        "name": "Arjun Patel",
        "email": "arjun.patel@student.com",
        "character_class": "Scholar",
        "level": 5,
        "xp": 2450
    }

def generate_study_sessions(count=10):
    """Generate demo study sessions."""
    subjects = ["Math", "Science", "English", "History", "Programming"]
    sessions = []
    
    for i in range(count):
        sessions.append({
            "subject": random.choice(subjects),
            "duration_minutes": random.randint(30, 120),
            "quality_score": random.uniform(6.0, 10.0)
        })
    
    return sessions

def generate_ai_interactions(count=15):
    """Generate demo AI interactions."""
    tools = ["ChatGPT", "Copilot", "Gemini", "Claude"]
    actions = [
        "Verify answer",
        "Explain concept",
        "Help understand",
        "Improve output",
        "Direct answer"
    ]
    reflections = [
        "Learned new approach",
        "Understood better",
        "Applied in problem",
        "Verified my thinking",
        ""
    ]
    
    interactions = []
    for i in range(count):
        interactions.append({
            "tool": random.choice(tools),
            "action": random.choice(actions),
            "reflection": random.choice(reflections)
        })
    
    return interactions

def generate_daily_metrics(days=7):
    """Generate demo daily metrics."""
    metrics = []
    
    for i in range(days):
        metrics.append({
            "date": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"),
            "sleep_hours": random.uniform(6.0, 9.0),
            "study_hours": random.uniform(1.0, 4.0),
            "focus_time": random.randint(60, 240),
            "reading_minutes": random.randint(10, 60)
        })
    
    return metrics

def generate_quiz_scores(count=5):
    """Generate demo quiz scores."""
    subjects = ["Math", "Science", "English", "History", "Programming"]
    scores = []
    
    for i in range(count):
        scores.append({
            "subject": random.choice(subjects),
            "score": random.uniform(65.0, 95.0)
        })
    
    return scores
