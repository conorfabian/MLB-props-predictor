import { useState, useEffect } from 'react'
import { TrendingUp } from 'lucide-react'
import BetCard from './BetCard'

const TodaysBetsPage = () => {
  const [bets, setBets] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchBets = async () => {
      try {
        setLoading(true)
        const response = await fetch(`${import.meta.env.VITE_API_URL}/api/bets`)
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        
        const result = await response.json()
        // Sort bets by confidence score in descending order (highest to lowest)
        const sortedBets = (result.data || []).sort((a, b) => b.confidence - a.confidence)
        setBets(sortedBets)
        setError(null)
      } catch (err) {
        console.error('Error fetching bets:', err)
        setError('Failed to load bets. Please try again later.')
        setBets([])
      } finally {
        setLoading(false)
      }
    }

    fetchBets()
  }, [])

  if (loading) {
    return (
      <div className="min-h-screen px-4 pb-12">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-8 sm:mb-12">
            <h1 className="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
              <span className="glow-text">Today's</span>
              <span className="text-white"> Top Bets</span>
            </h1>
            <p className="text-gray-300 text-base sm:text-lg max-w-2xl mx-auto px-4">
              AI-curated prop bets with the highest confidence scores for today's MLB games
            </p>
          </div>
          <div className="text-center">
            <div className="glass-card inline-block px-8 py-6">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-400 mx-auto mb-4"></div>
              <p className="text-gray-300">Loading today's top bets...</p>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen px-4 pb-12">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-8 sm:mb-12">
            <h1 className="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
              <span className="glow-text">Today's</span>
              <span className="text-white"> Top Bets</span>
            </h1>
            <p className="text-gray-300 text-base sm:text-lg max-w-2xl mx-auto px-4">
              AI-curated prop bets with the highest confidence scores for today's MLB games
            </p>
          </div>
          <div className="text-center">
            <div className="glass-card inline-block px-8 py-6">
              <p className="text-red-400 mb-4">{error}</p>
              <button 
                onClick={() => window.location.reload()} 
                className="btn-primary"
              >
                Try Again
              </button>
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen px-4 pb-12">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8 sm:mb-12">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
            <span className="glow-text">Today's</span>
            <span className="text-white"> Top Bets</span>
          </h1>
          <p className="text-gray-300 text-base sm:text-lg max-w-2xl mx-auto px-4">
            AI-curated prop bets ranked by confidence score for today's MLB games
          </p>
          <div className="mt-6 glass-card inline-block px-4 sm:px-6 py-3">
            <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-4 text-xs sm:text-sm">
              <div className="flex items-center">
                <div className="w-2 h-2 sm:w-3 sm:h-3 bg-green-400 rounded-full mr-1 sm:mr-2"></div>
                <span className="text-gray-300">High (80%+)</span>
              </div>
              <div className="flex items-center">
                <div className="w-2 h-2 sm:w-3 sm:h-3 bg-yellow-400 rounded-full mr-1 sm:mr-2"></div>
                <span className="text-gray-300">Medium (70-79%)</span>
              </div>
              <div className="flex items-center">
                <div className="w-2 h-2 sm:w-3 sm:h-3 bg-orange-400 rounded-full mr-1 sm:mr-2"></div>
                <span className="text-gray-300">Moderate (60-69%)</span>
              </div>
            </div>
          </div>
        </div>

        {/* Bets Grid */}
        {bets.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
            {bets.map((bet, index) => (
              <BetCard key={bet.id} bet={bet} index={index} />
            ))}
          </div>
        ) : (
          <div className="text-center">
            <div className="glass-card inline-block px-8 py-6">
              <p className="text-gray-300">No bets available at the moment.</p>
            </div>
          </div>
        )}

        {/* Bottom CTA */}
        <div className="mt-8 sm:mt-12 text-center glass-card p-6 sm:p-8">
          <h2 className="text-xl sm:text-2xl font-bold text-white mb-4">Want More Predictions?</h2>
          <p className="text-gray-300 mb-6 text-sm sm:text-base">
            Get access to premium analytics, live updates, and exclusive insider insights
          </p>
          <button className="btn-primary">
            <TrendingUp className="h-4 w-4 sm:h-5 sm:w-5 mr-2" />
            Upgrade to Premium
          </button>
        </div>
      </div>
    </div>
  )
}

export default TodaysBetsPage 