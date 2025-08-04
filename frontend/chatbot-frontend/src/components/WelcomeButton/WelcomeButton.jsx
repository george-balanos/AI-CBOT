import { useState } from "react"

export default function WelcomeButton({onWelcome}){
    const [clicked, setClicked] = useState(false)

    const handleClick = () => {
        setClicked(true)
        onWelcome()
    }

    return (
        <button 
            className={`welcome-button ${clicked ? 'clicked' : ''}`}
            onClick={handleClick}
            disabled={clicked}
        ></button>
    )
}