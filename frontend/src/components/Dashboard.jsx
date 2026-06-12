import React from 'react';

function Dashboard({ studentData }) {
  return (
    <div className="dashboard">
      <h2>Welcome to Your Growth Dashboard</h2>
      
      {studentData ? (
        <>
          <div className="dashboard-grid">
            <div className="card">
              <h3>📚 Today's Learning</h3>
              <p>Complete your daily quests to improve your skills</p>
              <div className="card-stat">30 min Math + 15 min Reading</div>
            </div>

            <div className="card">
              <h3>🎯 Your Goals</h3>
              <p>Working towards:</p>
              <div className="card-stat">Score 90% in Maths</div>
            </div>

            <div className="card">
              <h3>🏃 Activity Goal</h3>
              <p>Stay active and healthy</p>
              <div className="card-stat">45 min completed today</div>
            </div>

            <div className="card">
              <h3>🤖 AI Usage</h3>
              <p>Responsible AI tracking</p>
              <div className="card-stat">🟢 90% Smart Use</div>
            </div>
          </div>

          <div className="daily-quest">
            <h3>✨ Today's Quest</h3>
            <div className="quest-item">
              <input type="checkbox" /> 30 min Math Study
            </div>
            <div className="quest-item">
              <input type="checkbox" /> 15 min Reading
            </div>
            <div className="quest-item">
              <input type="checkbox" /> 10 min Walking
            </div>
            <div className="quest-item">
              <input type="checkbox" /> 1 Critical Thinking Challenge
            </div>
            <p className="xp-reward">🎁 Earn 150 XP when complete!</p>
          </div>
        </>
      ) : (
        <p>Loading your growth dashboard...</p>
      )}
    </div>
  );
}

export default Dashboard;
