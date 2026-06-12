# GrowAi Setup Guide

## 🚀 Quick Start

### Backend Setup

1. **Create virtual environment:**
```bash
cd backend
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the server:**
```bash
python main.py
```

Server will be available at: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

### Frontend Setup

1. **Install dependencies:**
```bash
cd frontend
npm install
```

2. **Start development server:**
```bash
npm start
```

Frontend will be available at: `http://localhost:3000`

---

## 📚 API Endpoints

### Student Management
- `POST /api/students/` - Create new student
- `GET /api/students/{student_id}` - Get student profile
- `PUT /api/students/{student_id}` - Update student

### Learning Agent
- `POST /api/agents/{student_id}/learning/log-session` - Log study session
- `POST /api/agents/{student_id}/learning/log-quiz` - Log quiz score
- `GET /api/agents/{student_id}/learning/analytics` - Get learning analytics
- `GET /api/agents/{student_id}/learning/recommendation` - Get learning recommendation

### AI Usage Agent
- `POST /api/agents/{student_id}/ai-usage/log-interaction` - Log AI interaction
- `GET /api/agents/{student_id}/ai-usage/report` - Get AI usage report
- `GET /api/agents/{student_id}/ai-usage/recommendation` - Get recommendation

### Activity Agent
- `POST /api/agents/{student_id}/activity/log` - Log physical activity
- `GET /api/agents/{student_id}/activity/break-recommendation/{duration}` - Get break recommendation
- `GET /api/agents/{student_id}/activity/daily-goal` - Get activity goals
- `GET /api/agents/{student_id}/activity/analytics` - Get activity analytics

### Game Agent
- `POST /api/agents/{student_id}/game/create-mission` - Create mission
- `POST /api/agents/{student_id}/game/complete-mission/{mission_id}` - Complete mission
- `GET /api/agents/{student_id}/game/stats` - Get game stats
- `GET /api/agents/{student_id}/game/mission-board` - Get mission board

### Habit Coach Agent
- `POST /api/agents/{student_id}/habits/log-daily` - Log daily metrics
- `GET /api/agents/{student_id}/habits/feedback` - Get habit feedback
- `GET /api/agents/{student_id}/habits/analytics` - Get habit analytics
- `GET /api/agents/{student_id}/habits/weekly-summary` - Get weekly summary

### Goal Planner Agent
- `POST /api/agents/{student_id}/goals/create` - Create goal
- `POST /api/agents/{student_id}/goals/{goal_id}/update-progress` - Update goal progress
- `GET /api/agents/{student_id}/goals/dashboard` - Get goal dashboard
- `GET /api/agents/{student_id}/goals/weekly-review` - Get weekly review

### Multi-Agent Dashboard
- `GET /api/agents/{student_id}/dashboard` - Get complete dashboard

### Missions
- `GET /api/missions/` - Get all missions
- `GET /api/missions/{mission_id}` - Get specific mission
- `GET /api/missions/by-subject/{subject}` - Get missions by subject
- `GET /api/missions/by-difficulty/{difficulty}` - Get missions by difficulty

### Progress Tracking
- `POST /api/progress/{student_id}` - Record progress
- `GET /api/progress/{student_id}` - Get progress history
- `GET /api/progress/{student_id}/category/{category}` - Get progress by category
- `GET /api/progress/{student_id}/summary` - Get progress summary

---

## 🎓 Testing the API

### 1. Create a Student
```bash
curl -X POST http://localhost:8000/api/students/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Arjun Patel",
    "email": "arjun@student.com"
  }'
```

### 2. Log a Study Session
```bash
curl -X POST http://localhost:8000/api/agents/{student_id}/learning/log-session \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Math",
    "duration_minutes": 45,
    "quality_score": 8.5
  }'
```

### 3. Log AI Interaction
```bash
curl -X POST http://localhost:8000/api/agents/{student_id}/ai-usage/log-interaction \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "ChatGPT",
    "action": "Verify answer",
    "reflection": "Understood the concept better"
  }'
```

### 4. Get Complete Dashboard
```bash
curl http://localhost:8000/api/agents/{student_id}/dashboard
```

---

## 🏗️ Architecture Overview

```
GrowAi/
├── Backend (FastAPI)
│   ├── agents/           # 6 AI agents
│   ├── routes/           # API endpoints
│   ├── models/           # Data models
│   ├── foundry_iq/       # Microsoft IQ integration
│   └── main.py           # FastAPI app
│
├── Frontend (React)
│   ├── components/       # React components
│   ├── api/              # API client
│   ├── App.jsx          # Main app
│   └── index.css        # Styles
│
├── Database
│   └── schema.sql       # PostgreSQL schema
│
└── docs/
    └── API documentation
```

---

## 🔗 Microsoft Foundry IQ Integration

Foundry IQ is integrated as the memory and context layer:

```python
from backend.foundry_iq import FoundryIQIntegration

foundry = FoundryIQIntegration(api_key="your_key")

# Store student history
foundry.store_student_history(student_id, {
    "study_patterns": {...},
    "ai_usage": {...},
    "achievements": [...]
})

# Retrieve for personalized coaching
context = foundry.retrieve_student_context(student_id)
coaching = foundry.generate_personalized_coaching(student_id, "learning")
```

---

## 📝 Environment Variables

Create `.env` file in project root:

```
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
DATABASE_URL=postgresql://user:password@localhost:5432/growai
OPENAI_API_KEY=your_key
FOUNDRY_IQ_API_KEY=your_key
REACT_APP_API_URL=http://localhost:8000
```

---

## 🚀 Deployment

### Backend
```bash
# Using Gunicorn
gunicorn backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

### Frontend
```bash
# Build production bundle
npm run build
```

---

## 🆘 Troubleshooting

### Port already in use
```bash
# Find process using port 8000
lsof -i :8000
# Kill process
kill -9 <PID>
```

### CORS errors
Backend already has CORS enabled for all origins. If issues persist, check:
- Backend running on correct port
- Frontend URL matches CORS configuration

### Module import errors
```bash
# Make sure you're in the right directory
cd backend
pip install -r requirements.txt
```

---

## 📞 Support

For issues or questions:
- Check API docs: http://localhost:8000/docs
- Review code in `backend/routes/`
- Check agent implementations in `backend/agents/`

---

**Built with ❤️ for Agents League Hackathon 2026**
