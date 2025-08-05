import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function UsernameBox({ welcomeTextMoved }) {
  const [delayedClass, setDelayedClass] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (welcomeTextMoved) {
      const timer = setTimeout(() => {
        setDelayedClass(true);
      }, 10);

      return () => clearTimeout(timer);
    }
  }, [welcomeTextMoved]); // This effect runs whenever "welcomeTextMoved" changes

  function handleSubmit(event) {
    event.preventDefault();

    const username = event.target.elements.username.value;

    fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({username: username})
    })
    .then(response => response.json())
    .then(data => {
        console.log("Backend says: ", data["message"])

        navigate("/chat", {state: {username}});

    })
    .catch(err => {
        console.error("Something went wrong: ", err)
    })

  }

  return (
    <div className={`credential-wrapper ${delayedClass ? 'credential-wrapper-on' : ''}`}>
      <label htmlFor="username">Enter Your Username</label>
      <form onSubmit={handleSubmit} id="login-form">
        <input type="text" name="username" id="username-box" />
        <button type="submit" id="login-button">Enter</button>
      </form>
    </div>
  );
}
