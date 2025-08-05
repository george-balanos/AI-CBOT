import { useState } from 'react';
import WelcomeButton from '../WelcomeButton/WelcomeButton'
import '../WelcomeButton/WelcomeButton.css'

import UsernameBox from '../UsernameBox/UsernameBox'
import '../UsernameBox/UsernameBox.css'

function WelcomePage() {
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

export default WelcomePage;
