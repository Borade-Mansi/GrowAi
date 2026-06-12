// API client for frontend

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

class APIClient {
  async request(method, endpoint, data = null) {
    const url = `${API_BASE_URL}${endpoint}`;
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
    };

    if (data) {
      options.body = JSON.stringify(data);
    }

    try {
      const response = await fetch(url, options);
      if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }

  // Student endpoints
  async createStudent(name, email) {
    return this.request('POST', '/api/students/', { name, email });
  }

  async getStudent(studentId) {
    return this.request('GET', `/api/students/${studentId}`);
  }

  // Agent endpoints
  async logStudySession(studentId, subject, durationMinutes, qualityScore) {
    return this.request('POST', `/api/agents/${studentId}/learning/log-session`, {
      subject,
      duration_minutes: durationMinutes,
      quality_score: qualityScore,
    });
  }

  async logAIInteraction(studentId, tool, action, reflection = '') {
    return this.request('POST', `/api/agents/${studentId}/ai-usage/log-interaction`, {
      tool,
      action,
      reflection,
    });
  }

  async logActivity(studentId, activityType, durationMinutes) {
    return this.request('POST', `/api/agents/${studentId}/activity/log`, {
      activity_type: activityType,
      duration_minutes: durationMinutes,
    });
  }

  async createMission(studentId, subject, difficulty = 'medium') {
    return this.request('POST', `/api/agents/${studentId}/game/create-mission`, null, {
      subject,
      difficulty,
    });
  }

  async completeMission(studentId, missionId) {
    return this.request('POST', `/api/agents/${studentId}/game/complete-mission/${missionId}`);
  }

  async logDailyMetrics(studentId, sleepHours, studyHours, focusTime, readingMinutes) {
    return this.request('POST', `/api/agents/${studentId}/habits/log-daily`, {
      sleep_hours: sleepHours,
      study_hours: studyHours,
      focus_time: focusTime,
      reading_minutes: readingMinutes,
    });
  }

  async createGoal(studentId, goalText, targetScore = null, subject = null, timelineDays = 30) {
    return this.request('POST', `/api/agents/${studentId}/goals/create`, null, {
      goal_text: goalText,
      target_score: targetScore,
      subject,
      timeline_days: timelineDays,
    });
  }

  // Dashboard
  async getDashboard(studentId) {
    return this.request('GET', `/api/agents/${studentId}/dashboard`);
  }

  async getGameStats(studentId) {
    return this.request('GET', `/api/agents/${studentId}/game/stats`);
  }

  async getLearningAnalytics(studentId) {
    return this.request('GET', `/api/agents/${studentId}/learning/analytics`);
  }

  async getAIUsageReport(studentId) {
    return this.request('GET', `/api/agents/${studentId}/ai-usage/report`);
  }

  async getActivityAnalytics(studentId) {
    return this.request('GET', `/api/agents/${studentId}/activity/analytics`);
  }

  // Missions
  async getAllMissions() {
    return this.request('GET', '/api/missions/');
  }

  async getMissionsBySubject(subject) {
    return this.request('GET', `/api/missions/by-subject/${subject}`);
  }
}

export default new APIClient();
