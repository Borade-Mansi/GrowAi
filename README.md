# 🚀 GrowAi - Personal Growth Agent Platform

**An AI mentor that helps students learn better, think independently, stay healthy, and grow every day.**

---

## 🎯 Mission

Transform how students learn by combining:
- 🤖 **Intelligent AI Agents** - Multi-agent system for personalized coaching
- 🎮 **Gamification** - Missions, badges, and character progression
- 📊 **Progress Tracking** - Evidence-based learning analytics
- 🧠 **Responsible AI** - Tracks and prevents AI dependency
- 💪 **Holistic Growth** - Learning + fitness + mental health

---

## 🏗️ Architecture: 6 AI Agents

### 1. **Learning Agent** 📚
- Tracks study sessions, homework, quizzes
- Identifies weak subjects
- Recommends revision strategies
- Provides personalized learning paths

### 2. **AI Usage Agent** 🤖
- Monitors ChatGPT, Copilot, Gemini, Claude usage
- Detects: Smart use (🟢) vs. Assisted Learning (🟡) vs. Dependency (🔴)
- Teaches responsible AI usage
- Prevents copy-paste learning

### 3. **Physical Activity Agent** 🏃
- Encourages breaks and movement
- Sends activity reminders after study sessions
- Tracks fitness impact on learning
- Science-backed: Movement improves memory

### 4. **Educational Game Agent** 🎮
- Converts learning into missions and quests
- Generates subject-specific challenges
- Awards badges and points
- Gamifies learning to increase engagement

### 5. **Habit Coach Agent** 🎯
- Tracks sleep, study hours, focus time
- Monitors reading habits
- Provides daily feedback
- Builds consistency streaks

### 6. **Goal Planner Agent** 📈
- Student sets goal: "Score 90% in Maths"
- Agent creates: Daily plans + Weekly targets + Monthly reviews
- Tracks progress
- Adjusts recommendations

---

## 🎮 Game World: Character Classes

Students don't see dashboards. They become characters:

- **Explorer** 🗺️ - Learns new topics
- **Builder** 🏗️ - Creates projects
- **Strategist** ♟️ - Uses AI intelligently
- **Scholar** 📖 - Maintains consistency
- **Master Creator** 👑 - Balances all skills

---

## 📋 Daily Missions

Every morning, students get a quest:

```
TODAY'S QUEST
✅ 30 min Math Study
✅ 15 min Reading
✅ 10 min Walking
✅ 1 Critical Thinking Challenge
✅ Use AI only after first attempt

Rewards: 150 XP + Progress toward weekly goal
```

---

## 🧠 Microsoft Foundry IQ Integration

Foundry IQ serves as the **memory and context layer**:

- Store study history
- Retrieve past learning patterns
- Access achievement records
- Provide personalized coaching based on historical data
- Reduce hallucination through grounded, cited recommendations

---

## 📊 Why This Project Wins

### Accuracy & Relevance (20%)
✅ Solves real education problem  
✅ Evidence-based approach  
✅ Meets hackathon requirements  

### Reasoning & Multi-step (20%)
✅ 6 agents collaborate and reason together  
✅ Complex decision-making  
✅ Multi-step problem solving  

### Creativity & Originality (15%)
✅ Unique game-world concept  
✅ Novel personal growth tracking  
✅ No competitors building this  

### User Experience (15%)
✅ Gamified interface  
✅ Character progression  
✅ Beautiful, demoable UI  

### Reliability & Safety (20%)
✅ Tracks responsible AI usage  
✅ Evidence-based recommendations  
✅ Solid error handling  

### Community Vote (10%)
✅ Students will love this  
✅ Shareable on Discord  
✅ Relatable impact  

---

## 🚀 Tech Stack

- **Backend:** Python (FastAPI)
- **Frontend:** React + TypeScript
- **Database:** PostgreSQL
- **AI:** OpenAI API
- **Microsoft IQ:** Foundry IQ
- **Deployment:** GitHub + Azure

---

## 📁 Project Structure

```
GrowAi/
├── backend/
│   ├── agents/
│   │   ├── learning_agent.py
│   │   ├── ai_usage_agent.py
│   │   ├── activity_agent.py
│   │   ├── game_agent.py
│   │   ├── habit_coach_agent.py
│   │   └── goal_planner_agent.py
│   ├── routes/
│   │   ├── students.py
│   │   ├── agents.py
│   │   ├── missions.py
│   │   └── progress.py
│   ├── foundry_iq/
│   │   └── integration.py
│   ├── models/
│   │   └── student.py
│   ├── utils/
│   │   └── demo_data.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── MissionBoard.jsx
│   │   │   ├── CharacterProfile.jsx
│   │   │   └── ProgressTracker.jsx
│   │   ├── api/
│   │   │   └── client.js
│   │   ├── App.jsx
│   │   └── index.css
│   └── package.json
├── database/
│   └── schema.sql
├── SETUP.md
├── README.md
└── .gitignore
```

---

## 🎬 Demo Video Script

```
SCENE 1: "The Problem"
- Student opens laptop, wants to learn Calculus
- Overwhelmed, pulls up ChatGPT, copies answers
- Screen time: 4 hours, learning: minimal

SCENE 2: "Meet GrowAi"
- Same student logs into GrowAi
- Sees character: "Scholar" with 65% progress
- Daily quest appears with 30-min Math mission

SCENE 3: "Multi-Agent Magic"
- Learning Agent: "Your weak spot is derivatives"
- Game Agent: "Complete 5 derivative challenges to unlock badge"
- Activity Agent: "After 30 min, take a 10-min walk break"
- AI Usage Agent: "Try solving first, then use ChatGPT to verify"

SCENE 4: "Progress Tracking"
- Dashboard shows:
  - 90% responsible AI usage
  - 5-day study streak
  - Math score improved 15%
  - 8 badges earned

SCENE 5: "The Impact"
- 2 weeks later: Student scores 85% on exam
- "GrowAi didn't just help me pass. It taught me HOW to learn."
```

---

## 🎯 Judging Rubric Checklist

- [x] **Accuracy & Relevance:** Real problem, evidence-based
- [x] **Reasoning & Multi-step:** 6 agents, complex logic
- [x] **Creativity & Originality:** Unique game-world + responsible AI tracking
- [x] **User Experience:** Gamified, polished, demoable
- [x] **Reliability & Safety:** Error handling, AI dependency detection
- [x] **Community Vote:** Student-centric, shareable, impactful

---

## 📅 Timeline

| Date | Task |
|------|------|
| June 12 | ✅ Project structure + agents scaffolding + API endpoints |
| June 13 | ✅ Agent logic + UI implementation + testing |
| June 14 | ✅ Polish + demo video + submit |

---

## 🤝 Microsoft IQ Integration

### Foundry IQ as Memory Layer

```python
# Store and retrieve student context
foundry_iq.store("student_history", {
    "study_patterns": learning_agent.patterns,
    "ai_usage": ai_usage_agent.metrics,
    "achievements": habit_coach_agent.badges,
    "goals": goal_planner_agent.objectives
})

# Agents retrieve context for personalized coaching
context = foundry_iq.retrieve("student_history", student_id)
coaching = habit_coach_agent.generate_personalized_feedback(context)
```

---

## 🎓 How This Scales

Future vision:
- **Age 10:** Learns healthy study habits
- **Age 13:** Masters responsible AI usage
- **Age 16:** Develops critical thinking
- **Age 18+:** Transitions to professional growth tracking
- **Lifelong:** Continuous learning companion

---

## 📞 Support & Community

- 💬 Discord: Agents League Arena
- 📚 Questions: Check `/SETUP.md`
- 🐛 Bugs: Create an issue

---

## 📝 License

MIT License - Built for Agents League Hackathon 2026

---

**Made with ❤️ for students who want to learn better, think independently, and grow every day.**

🚀 **Let's revolutionize education with AI!**
