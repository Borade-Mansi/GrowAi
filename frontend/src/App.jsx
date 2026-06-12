import React, { useState, useEffect } from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import MissionBoard from './components/MissionBoard';
import CharacterProfile from './components/CharacterProfile';
import ProgressTracker from './components/ProgressTracker';

function App() {
  const [currentView, setCurrentView] = useState('dashboard');
  const [studentData, setStudentData] = useState(null);

  useEffect(() => {
    // Fetch student data from backend
    const fetchStudentData = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/student');
        const data = await response.json();
        setStudentData(data);
      } catch (error) {
        console.error('Error fetching student data:', error);
      }
    };

    fetchStudentData();
  }, []);

  const renderView = () => {
    switch (currentView) {
      case 'dashboard':
        return <Dashboard studentData={studentData} />;
      case 'missions':
        return <MissionBoard studentData={studentData} />;
      case 'character':
        return <CharacterProfile studentData={studentData} />;
      case 'progress':
        return <ProgressTracker studentData={studentData} />;
      default:
        return <Dashboard studentData={studentData} />;
    }
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>🚀 GrowAi</h1>
        <p>Your Personal Growth Agent</p>
      </header>

      <nav className="app-nav">
        <button
          className={currentView === 'dashboard' ? 'active' : ''}
          onClick={() => setCurrentView('dashboard')}
        >
          📊 Dashboard
        </button>
        <button
          className={currentView === 'missions' ? 'active' : ''}
          onClick={() => setCurrentView('missions')}
        >
          🎮 Missions
        </button>
        <button
          className={currentView === 'character' ? 'active' : ''}
          onClick={() => setCurrentView('character')}
        >
          👤 Character
        </button>
        <button
          className={currentView === 'progress' ? 'active' : ''}
          onClick={() => setCurrentView('progress')}
        >
          📈 Progress
        </button>
      </nav>

      <main className="app-main">
        {renderView()}
      </main>
    </div>
  );
}

export default App;
