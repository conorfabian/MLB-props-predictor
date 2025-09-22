import { Link } from 'react-router-dom'
import { TrendingUp, Target, Brain, Zap, Shield, BarChart3 } from 'lucide-react'

const LandingPage = () => {
  const features = [
    {
      icon: <Brain className="h-8 w-8 text-blue-400" />,
      title: "AI-Powered Predictions",
      description: "Advanced machine learning algorithms analyze player performance, weather, and historical data to generate accurate prop predictions."
    },
    {
      icon: <Target className="h-8 w-8 text-purple-400" />,
      title: "High Confidence Bets",
      description: "Each prediction comes with a confidence score, helping you make informed decisions with the most reliable data."
    },
    {
      icon: <BarChart3 className="h-8 w-8 text-pink-400" />,
      title: "Real-Time Analytics",
      description: "Live updates on player stats, injury reports, and lineup changes to ensure you have the most current information."
    },
    {
      icon: <Zap className="h-8 w-8 text-yellow-400" />,
      title: "Lightning Fast",
      description: "Get instant access to today's top prop bets with real-time processing and updates throughout the day."
    },
    {
      icon: <Shield className="h-8 w-8 text-green-400" />,
      title: "Data-Driven Insights",
      description: "Backed by comprehensive statistical analysis and verified historical performance data for maximum reliability."
    },
    {
      icon: <TrendingUp className="h-8 w-8 text-orange-400" />,
      title: "Proven Results",
      description: "Track record of successful predictions with transparent performance metrics and detailed result breakdowns."
    }
  ]

  return (
    <div className="min-h-screen px-4 pb-12">
      {/* Hero Section */}
      <div className="max-w-6xl mx-auto pt-8">
        <div className="text-center mb-16">
          <h1 className="text-6xl md:text-7xl font-bold mb-6 floating">
            <span className="glow-text">MLB Props</span>
            <br />
            <span className="text-white">Predictor</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto leading-relaxed">
            Harness the power of AI to identify the most profitable MLB player prop bets. 
            Get data-driven predictions with confidence scores to maximize your winning potential.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <Link to="/todays-bets" className="btn-primary glow-effect">
              <Target className="h-5 w-5 mr-2" />
              View Today's Bets
            </Link>
            <button className="btn-secondary">
              Learn More
            </button>
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          {features.map((feature, index) => (
            <div key={index} className="glass-card-hover p-6 floating" style={{animationDelay: `${index * 0.2}s`}}>
              <div className="mb-4">{feature.icon}</div>
              <h3 className="text-xl font-semibold text-white mb-3">{feature.title}</h3>
              <p className="text-gray-300 leading-relaxed">{feature.description}</p>
            </div>
          ))}
        </div>

        {/* Stats Section */}
        <div className="glass-card p-8 text-center mb-16">
          <h2 className="text-3xl font-bold text-white mb-8">Why Choose Our Predictions?</h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div>
              <div className="text-4xl font-bold glow-text mb-2">85%</div>
              <p className="text-gray-300">Average Accuracy</p>
            </div>
            <div>
              <div className="text-4xl font-bold glow-text mb-2">15+</div>
              <p className="text-gray-300">Data Sources</p>
            </div>
            <div>
              <div className="text-4xl font-bold glow-text mb-2">24/7</div>
              <p className="text-gray-300">Real-Time Updates</p>
            </div>
          </div>
        </div>

        {/* CTA Section */}
        <div className="glass-card p-8 text-center liquid-gradient">
          <h2 className="text-3xl font-bold text-white mb-4">Ready to Start Winning?</h2>
          <p className="text-gray-300 mb-6 max-w-2xl mx-auto">
            Join thousands of successful bettors who trust our AI-powered predictions 
            to make informed decisions and maximize their profits.
          </p>
          <Link to="/todays-bets" className="btn-primary glow-effect">
            <Target className="h-5 w-5 mr-2" />
            Get Today's Predictions
          </Link>
        </div>
      </div>
    </div>
  )
}

export default LandingPage 