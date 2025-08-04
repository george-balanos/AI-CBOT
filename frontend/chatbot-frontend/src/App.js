import { useState } from 'react';
import './App.css';
import WelcomeButton from './components/WelcomeButton/WelcomeButton'
import './components/WelcomeButton/WelcomeButton.css'

import UsernameBox from './components/UsernameDiv/UsernameBox'
import './components/UsernameDiv/UsernameBox.css'

function App() {
  const [welcomeTextMoved, setWelcomeTextMoved] = useState(false)

  const handleWelcomeButton = () => {
    setWelcomeTextMoved(true)
  }

  return (
    <>
      <div className="wrapper">
        <div className={`welcome-text ${welcomeTextMoved ? "welcome-text-moved" : ''}`}>Welcome to AI-CBOT!</div>

        {welcomeTextMoved && <UsernameBox welcomeTextMoved={welcomeTextMoved}/>}

        <WelcomeButton onWelcome={handleWelcomeButton}/>
      </div>
    </>
  );
}

export default App;
