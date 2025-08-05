import { useEffect,useState } from "react";
import { useLocation } from "react-router-dom"

function HumanResponse({message}) {
    return (
        <>
            <div className="message-wrapper">
                <div className="icon">
                    <img src="user.png" alt="user_icon" />
                </div>
                <div className="message-text">
                    {message}
                </div>
            </div>
        </>
    )
}

function SystemResponse({message}) {
    return (
        <>
            <div className="message-wrapper">
                <div className="icon">
                    <img src="chat.png" alt="user_icon" />
                </div>
                <div className="message-text system-text">
                    {message}
                </div>
            </div>
        </>
    )
}

export default function ChatBoard() {
    const location = useLocation();
    const username = location.state?.username;
    
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        if (!username) return;

        fetch(`http://localhost:8000/chat/messages?username=${username}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            // setMessages(data["messages"])
            setMessages(data["messages"].slice(1));
        })
        .catch(err => {
            console.log("Something went wrong: ", err)
        })
    }, [username])

    const handleSubmit = (event) => {
        event.preventDefault();

        const user_question = event.target.elements.user_query.value;
        if (!user_question.trim()) return; // ignore empty

        setMessages(prevMessages => [
            ...prevMessages,
            { sender: "human", message: user_question, timestamp: new Date().toISOString() }
        ]);

        event.target.elements.user_query.value = ""

        fetch("http://localhost:8000/chat/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username, 
                user_question: user_question
            })
        })
        .then(response => response.json())
        .then(data => {
            setMessages(prevMessages => [
                ...prevMessages,
                { sender: "system", message: data["response"], timestamp: new Date().toISOString() }
            ]);
        })
        .catch(err => {
            console.error("Something went wrong: ", err)
        })

    }

    return (
        <>
            <div className="user-info-section">
                <div className="logo-text">AI-CBOT</div>
                <div className="user-info-right">
                    <div className="login-circle"></div>
                    <div className="username-text">{username}</div>
                </div>
            </div>

            <div className="wrapper">
                <div className="input-box">
                    <form action="submit" onSubmit={handleSubmit}>
                        <input type="text" name="user_query" id="user_question" placeholder="Ask Anything!"/>
                    </form>
                </div>
                <div className="display-panel">
                    {[...messages].length > 0 ? (
                    [...messages]
                        .sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp))
                        .map((msg, index) =>
                        msg.sender === "human" ? (
                            <HumanResponse key={index} message={msg.message} />
                        ) : (
                            <SystemResponse key={index} message={msg.message} />
                        )
                        )
                    ) : null}
                </div>
            </div>
        </>
    )

}