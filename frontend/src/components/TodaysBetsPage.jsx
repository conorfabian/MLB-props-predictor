import { useState } from 'react'
import { TrendingUp } from 'lucide-react'
import BetCard from './BetCard'

const TodaysBetsPage = () => {
  // Mock data for demo purposes
  const [bets] = useState([
    {
      id: 1,
      playerName: "Aaron Judge",
      team: "NYY",
      position: "OF",
      photo: "https://via.placeholder.com/120x120/1e293b/ffffff?text=AJ",
      bet: "Over 1.5 Total Bases",
      odds: "+110",
      confidence: 89,
      description: "Judge has exceeded 1.5 total bases in 8 of his last 10 games. Facing a left-handed pitcher with a 5.2 ERA against righties this season.",
      reasoning: "Strong recent form, favorable matchup vs LHP, excellent home stats"
    },
    {
      id: 2,
      playerName: "Ronald Acuña Jr.",
      team: "ATL",
      position: "OF",
      photo: "https://via.placeholder.com/120x120/1e293b/ffffff?text=RA",
      bet: "Over 0.5 Stolen Bases",
      odds: "+125",
      confidence: 82,
      description: "Acuña has stolen 12 bases in his last 20 games. Opposing catcher has allowed 15 stolen bases in last 10 games with below-average pop time.",
      reasoning: "Elite speed, favorable catcher matchup, aggressive base running recently"
    },
    {
      id: 3,
      playerName: "Mookie Betts",
      team: "LAD",
      position: "OF",
      photo: "https://via.placeholder.com/120x120/1e293b/ffffff?text=MB",
      bet: "Over 1.5 Hits",
      odds: "+105",
      confidence: 76,
      description: "Betts is hitting .340 over his last 15 games and has faced today's starting pitcher 3 times with 2 multi-hit games.",
      reasoning: "Hot streak, positive historical matchup, consistent contact hitter"
    },
    {
      id: 4,
      playerName: "Vladimir Guerrero Jr.",
      team: "TOR",
      position: "1B",
      photo: "https://via.placeholder.com/120x120/1e293b/ffffff?text=VG",
      bet: "Over 0.5 Home Runs",
      odds: "+180",
      confidence: 71,
      description: "Vlad Jr. has 5 HRs in his last 8 games. Today's pitcher allows 1.8 HR/9 and has surrendered 3 HRs to righties in last 2 starts.",
      reasoning: "Power surge, pitcher vulnerability to righties, favorable wind conditions"
    },
    {
      id: 5,
      playerName: "Fernando Tatis Jr.",
      team: "SD",
      position: "SS",
      photo: "https://via.placeholder.com/120x120/1e293b/ffffff?text=FT",
      bet: "Over 1.5 RBIs",
      odds: "+140",
      confidence: 68,
      description: "Tatis is batting .380 with RISP this month. Expected to bat 3rd with strong on-base hitters ahead of him in the lineup.",
      reasoning: "Clutch hitting with RISP, favorable lineup position, quality base runners"
    },
    {
      id: 6,
      playerName: "Freddie Freeman",
      team: "LAD",
      position: "1B",
      photo: "https://via.placeholder.com/120x120/1e293b/ffffff?text=FF",
      bet: "Under 0.5 Strikeouts",
      odds: "-105",
      confidence: 84,
      description: "Freeman has struck out only 3 times in his last 15 games. Excellent contact rate vs today's starting pitcher (12% K rate in 25 PAs).",
      reasoning: "Elite contact skills, favorable pitcher history, low strikeout trend"
    }
  ])

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
            AI-curated prop bets with the highest confidence scores for today's MLB games
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
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
          {bets.map((bet, index) => (
            <BetCard key={bet.id} bet={bet} index={index} />
          ))}
        </div>

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