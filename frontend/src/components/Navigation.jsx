import { Link, useLocation } from 'react-router-dom'
import { BarChart3, Target } from 'lucide-react'

const Navigation = () => {
  const location = useLocation()

  return (
    <nav className="glass-card m-4 p-4 sticky top-4 z-50">
      <div className="flex items-center justify-between max-w-6xl mx-auto">
        <div className="flex items-center space-x-2">
          <div className="p-2 glass-card glow-effect">
            <BarChart3 className="h-6 w-6 text-blue-400" />
          </div>
          <h1 className="text-xl font-bold glow-text">MLB Props Predictor</h1>
        </div>
        
        <div className="flex items-center space-x-4">
          <Link
            to="/"
            className={`btn-secondary ${
              location.pathname === '/' ? 'bg-white/10 text-white' : ''
            }`}
          >
            Home
          </Link>
          <Link
            to="/todays-bets"
            className={`btn-secondary ${
              location.pathname === '/todays-bets' ? 'bg-white/10 text-white' : ''
            }`}
          >
            <Target className="h-4 w-4 mr-2" />
            Today's Bets
          </Link>
        </div>
      </div>
    </nav>
  )
}

export default Navigation 