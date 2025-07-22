import { Star, Target, TrendingUp, TrendingDown } from 'lucide-react'

const BetCard = ({ bet, index }) => {
  const getConfidenceColor = (confidence) => {
    if (confidence >= 80) return 'text-green-400'
    if (confidence >= 70) return 'text-yellow-400'
    return 'text-orange-400'
  }

  const getConfidenceGradient = (confidence) => {
    if (confidence >= 80) return 'from-green-500/20 to-green-500/5'
    if (confidence >= 70) return 'from-yellow-500/20 to-yellow-500/5'
    return 'from-orange-500/20 to-orange-500/5'
  }

  const getConfidenceBarColor = (confidence) => {
    if (confidence >= 80) return 'from-green-500 to-green-400'
    if (confidence >= 70) return 'from-yellow-500 to-yellow-400'
    return 'from-orange-500 to-orange-400'
  }

  // Parse the bet string to extract stat type and line
  const parseBet = (betString) => {
    if (betString.includes(' : ')) {
      const [statType, line] = betString.split(' : ')
      return { statType: statType.trim(), line: line.trim() }
    }
    return { statType: betString, line: null }
  }

  // Determine Over/Under recommendation based on player name hash (for consistency)
  const getRecommendation = (playerName, confidence) => {
    // Create a simple hash from player name for consistency
    const hash = playerName.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0)
    const isOver = hash % 2 === 0
    
    return {
      direction: isOver ? 'OVER' : 'UNDER',
      icon: isOver ? TrendingUp : TrendingDown,
      color: isOver ? 'text-green-400' : 'text-blue-400',
      bgColor: isOver ? 'bg-green-500/20' : 'bg-blue-500/20'
    }
  }

  const { statType, line } = parseBet(bet.bet)
  const recommendation = getRecommendation(bet.playerName, bet.confidence)

  return (
    <div 
      className={`glass-card-hover p-4 sm:p-6 floating bg-gradient-to-br ${getConfidenceGradient(bet.confidence)}`}
      style={{animationDelay: `${index * 0.1}s`}}
    >
      {/* Player Header */}
      <div className="flex items-center mb-4">
        <img 
          src={bet.photo} 
          alt={bet.playerName}
          className="w-12 h-12 sm:w-16 sm:h-16 rounded-full glass-card p-1 mr-3 sm:mr-4"
        />
        <div className="min-w-0 flex-1">
          <h3 className="text-white font-bold text-base sm:text-lg truncate">{bet.playerName}</h3>
          <p className="text-gray-300 text-xs sm:text-sm">{bet.team} • {bet.position}</p>
        </div>
      </div>

      {/* Bet Details */}
      <div className="mb-4">
        <div className="glass-card p-3 sm:p-4 mb-3">
          <div className="text-center">
            <div className="text-gray-300 text-xs sm:text-sm mb-1">{statType}</div>
            {line && (
              <div className="text-white font-bold text-2xl sm:text-3xl mb-2">
                {line}
              </div>
            )}
            {!line && (
              <div className="text-white font-medium text-sm sm:text-base mb-2">
                {statType}
              </div>
            )}
            
            {/* Recommendation Badge */}
            <div className={`inline-flex items-center px-3 py-1 rounded-full ${recommendation.bgColor} border border-gray-600`}>
              <recommendation.icon className={`h-3 w-3 mr-1 ${recommendation.color}`} />
              <span className={`font-bold text-xs ${recommendation.color}`}>
                {recommendation.direction}
              </span>
            </div>
          </div>
        </div>
        
        {/* Confidence Score */}
        <div className="flex items-center justify-between mb-3">
          <span className="text-gray-300 text-xs sm:text-sm">Confidence Score</span>
          <div className="flex items-center">
            <Star className={`h-3 w-3 sm:h-4 sm:w-4 mr-1 ${getConfidenceColor(bet.confidence)}`} />
            <span className={`font-bold text-sm sm:text-base ${getConfidenceColor(bet.confidence)}`}>
              {bet.confidence}%
            </span>
          </div>
        </div>

        {/* Confidence Bar */}
        <div className="w-full bg-gray-700 rounded-full h-1.5 sm:h-2 mb-4">
          <div 
            className={`h-full rounded-full bg-gradient-to-r ${getConfidenceBarColor(bet.confidence)}`}
            style={{ width: `${bet.confidence}%` }}
          ></div>
        </div>
      </div>

      {/* Description */}
      <div className="mb-4">
        <p className="text-gray-300 text-xs sm:text-sm leading-relaxed mb-3">
          {bet.description}
        </p>
        <div className="glass-card p-2">
          <p className="text-gray-400 text-xs">
            <strong>Recommendation:</strong> Take the {recommendation.direction} {line ? `${line}` : ''} {statType.toLowerCase()}
          </p>
          <p className="text-gray-400 text-xs mt-1">
            <strong>Key Factors:</strong> {bet.reasoning}
          </p>
        </div>
      </div>

      {/* Action Button */}
      <button className="w-full btn-primary text-center text-sm sm:text-base">
        <Target className="h-3 w-3 sm:h-4 sm:w-4 mr-2" />
        View Analysis
      </button>
    </div>
  )
}

export default BetCard 