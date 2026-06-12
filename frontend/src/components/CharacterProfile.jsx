import React from 'react';

function CharacterProfile({ studentData }) {
  return (
    <div className="character-profile">
      <h2>👤 Your Character</h2>

      <div className="character-info">
        <div className="character-class">
          <h3>🗺️ Explorer</h3>
          <p>Learns new topics and discovers knowledge</p>
        </div>

        <div className="character-stats">
          <div className="stat">
            <label>Level</label>
            <span className="stat-value">5</span>
          </div>
          <div className="stat">
            <label>XP</label>
            <span className="stat-value">2,450 / 2,500</span>
          </div>
          <div className="stat">
            <label>Badges</label>
            <span className="stat-value">8</span>
          </div>
          <div className="stat">
            <label>Study Streak</label>
            <span className="stat-value">5 days</span>
          </div>
        </div>
      </div>

      <div className="badges-section">
        <h3>🏆 Your Badges</h3>
        <div className="badges-grid">
          <div className="badge">Quick Learner</div>
          <div className="badge">Consistent Scholar</div>
          <div className="badge">AI Master</div>
          <div className="badge">Active Lifestyle</div>
        </div>
      </div>
    </div>
  );
}

export default CharacterProfile;
