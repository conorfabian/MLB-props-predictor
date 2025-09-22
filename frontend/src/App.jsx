import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import LandingPage from './components/LandingPage'
import TodaysBetsPage from './components/TodaysBetsPage'
import Navigation from './components/Navigation'
import './App.css'

function App() {
  return (
    <Router>
      <div 
        className="min-h-screen"
        style={{
          background: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%)',
          fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
        }}
      >
        <Navigation />
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/todays-bets" element={<TodaysBetsPage />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
