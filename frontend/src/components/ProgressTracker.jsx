import React from 'react';

function ProgressTracker({ studentData }) {
  return (
    <div className="progress-tracker">
      <h2>📈 Your Progress</h2>

      <div className="progress-items">
        <div className="progress-item">
          <h3>Math Goal: 90%</h3>
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: '75%' }}></div>
          </div>
          <p className="progress-text">75% Complete - 2 weeks to go</p>
        </div>

        <div className="progress-item">
          <h3>Study Consistency</h3>
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: '100%' }}></div>
          </div>
          <p className="progress-text">5-day streak maintained!</p>
        </div>

        <div className="progress-item">
          <h3>Responsible AI Usage</h3>
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: '90%' }}></div>
          </div>
          <p className="progress-text">90% smart AI use 🟢</p>
        </div>
      </div>

      <div className="insights">
        <h3>💡 Insights</h3>
        <ul>
          <li>Your math scores improved 15% after focusing on derivatives</li>
          <li>Walking breaks increased your focus time by 20%</li>
          <li>Consistent study habits are paying off!</li>
        </ul>
      </div>
    </div>
  );
}

export default ProgressTracker;
