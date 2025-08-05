import { Routes, Route } from "react-router-dom"

import WelcomePage from './components/WelcomePage/WelcomePage';
import './components/WelcomePage/WelcomePage.css'

import ChatBoard from './components/ChatBoard/ChatBoard'
import './components/ChatBoard/ChatBoard.css'

function App() {
  return (
    <Routes>
      <Route path="/" element={<WelcomePage />}></Route>
      <Route path="/chat" element={<ChatBoard />}></Route>
    </Routes>
  );
}

export default App;
