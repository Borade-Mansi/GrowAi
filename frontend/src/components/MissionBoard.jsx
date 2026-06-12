import React from 'react';

function MissionBoard({ studentData }) {
  const missions = [
    { id: 1, title: 'Solve 5 Math Problems', subject: 'Math', xp: 100, difficulty: 'medium' },
    { id: 2, title: 'Read 15 minutes', subject: 'Reading', xp: 75, difficulty: 'easy' },
    { id: 3, title: 'Challenge: Advanced Calculus', subject: 'Math', xp: 200, difficulty: 'hard' }
  ];

  return (
    <div className="mission-board">
      <h2>🎮 Mission Board</h2>
      <p>Complete missions to earn XP and badges!</p>

      <div className="missions-list">
        {missions.map((mission) => (
          <div key={mission.id} className="mission-card">
            <div className="mission-header">
              <h3>{mission.title}</h3>
              <span className={`difficulty ${mission.difficulty}`}>{mission.difficulty}</span>
            </div>
            <p className="mission-subject">{mission.subject}</p>
            <div className="mission-footer">
              <span className="xp-badge">+{mission.xp} XP</span>
              <button className="start-mission">Start Mission</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MissionBoard;
