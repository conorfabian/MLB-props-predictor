# MLB Props Predictor

A full-stack web application for predicting MLB player props using AI-powered analysis and live data integration.

## Project Overview

This application provides real-time MLB player prop predictions by combining multiple data sources including live odds from DraftKings and comprehensive player statistics from Baseball Reference. The system features a modern React frontend with a FastAPI backend that delivers data-driven betting insights.

## Current Status

✅ **Fully Functional Application**

The application is currently operational with:
- **Frontend**: Complete React UI with responsive design and routing
- **Backend**: FastAPI server with live data integration
- **Data Sources**: DraftKings API integration and MLB statistics via pybaseball
- **API**: Multiple endpoints serving real sports data
- **UI Components**: Landing page, betting predictions display, and player cards

## Technology Stack

### Frontend
- **React 18** with React Router DOM v7.6.3 for navigation
- **Vite** - Fast build tool and development server
- **Tailwind CSS 3.3.6** - Utility-first CSS framework with responsive design
- **Lucide React** - Modern icon library
- **PostCSS + Autoprefixer** - CSS processing

### Backend
- **FastAPI 0.104.1** - Modern, fast web framework
- **Uvicorn 0.24.0** - ASGI server with standard features
- **pybaseball** - MLB statistics and data retrieval
- **pandas** - Data manipulation and analysis
- **requests** - HTTP library for API calls
- **Supabase 2.3.0** - Database client (configured but not actively used)
- **python-dotenv** - Environment variable management

### Data Sources
- **DraftKings API** - Live betting odds and player props
- **Baseball Reference** - Historical and current player statistics
- **pybaseball** - Python library for MLB data access

## Quick Start

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8 or higher
- npm or yarn
- pip

### 1. Clone and Setup

```bash
git clone <repository-url>
cd MLB-props-predictor
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (optional for basic functionality)
cp env.example .env
# Edit .env with your Supabase credentials if needed

# Run the backend server
python main.py
```

Backend runs at `http://localhost:8000`

### 3. Frontend Setup

```bash
# Navigate to frontend directory (in a new terminal)
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

Frontend runs at `http://localhost:5173`

## Project Structure

```
MLB-props-predictor/
├── README.md                    # This file
├── data/                        # Data storage directory
├── backend/                     # FastAPI backend application
│   ├── main.py                 # FastAPI app with API endpoints
│   ├── helpers.py              # Data fetching and processing functions
│   ├── database.py             # Supabase database client setup
│   ├── requirements.txt        # Python dependencies
│   ├── env.example            # Environment variables template
│   ├── venv/                  # Python virtual environment
│   └── README.md              # Backend documentation
└── frontend/                   # React frontend application
    ├── src/
    │   ├── App.jsx            # Main app component with routing
    │   ├── main.jsx           # React entry point
    │   ├── index.css          # Global styles with Tailwind
    │   ├── App.css            # Component-specific styles
    │   └── components/
    │       ├── LandingPage.jsx        # Homepage with hero and features
    │       ├── TodaysBetsPage.jsx     # Betting predictions page
    │       ├── BetCard.jsx           # Individual bet display component
    │       └── Navigation.jsx        # Navigation header
    ├── public/                # Static assets
    ├── index.html            # HTML template
    ├── package.json          # Dependencies and scripts
    ├── tailwind.config.js    # Tailwind configuration
    ├── postcss.config.js     # PostCSS configuration
    ├── vite.config.js        # Vite configuration
    └── README.md             # Frontend documentation
```

## API Endpoints

### Currently Implemented

**Base URL**: `http://localhost:8000`

#### 1. Health Check
- **GET** `/`
- Returns API status
- **Response**: `{"message": "MLB Props Predictor API is running"}`

#### 2. Live Sports Data
- **GET** `/get-sports-data`
- Fetches current betting odds from DraftKings API
- **Response**: Array of player betting data with odds

#### 3. Pitching Statistics
- **GET** `/get-pitching-stats`
- Retrieves MLB pitching statistics for 2025 season
- **Response**: Statistical data summary with player information

#### 4. Formatted Betting Data
- **GET** `/api/bets`
- Returns formatted betting predictions for frontend consumption
- **Response**: 
```json
{
  "message": "Live betting data from DraftKings",
  "data": [
    {
      "id": 1,
      "playerName": "Player Name",
      "team": "TBD",
      "position": "TBD",
      "photo": "placeholder_url",
      "bet": "TBD",
      "odds": "TBD",
      "confidence": 89,
      "description": "TBD",
      "reasoning": "TBD"
    }
  ]
}
```

### API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Frontend Features

### Current Pages

#### 1. Landing Page (`/`)
- Hero section with animated elements
- Feature showcase grid
- Statistics display
- Call-to-action sections
- Responsive design with glass morphism effects

#### 2. Today's Bets Page (`/todays-bets`)
- Live betting predictions display
- Player cards with confidence scores
- Color-coded confidence indicators
- Real-time data loading states
- Error handling and retry functionality

### UI Components

#### BetCard Component
- Player photo and information
- Betting details and odds
- Confidence score with visual indicators
- Color-coded confidence levels (Green: 80%+, Yellow: 70-79%, Orange: 60-69%)
- Responsive design

#### Navigation Component
- Route navigation between pages
- Modern design with glass effects

## Dependencies

### Backend (requirements.txt)
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-dotenv==1.0.0
python-multipart==0.0.6
supabase==2.3.0
pybaseball
pandas
requests
```

### Frontend (package.json)
```json
{
  "dependencies": {
    "lucide-react": "^0.525.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^7.6.3"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.16",
    "eslint": "^8.55.0",
    "tailwindcss": "^3.3.6",
    "vite": "^5.0.8"
  }
}
```

## Data Integration

### DraftKings API
- Live betting odds and player props
- Real-time market data
- Player-specific betting information
- Automated data fetching with proper headers

### Baseball Reference (via pybaseball)
- Historical player statistics
- Current season data
- Pitching and batting statistics
- Rate limiting and caching support

## Environment Setup

### Backend Environment Variables

Create a `.env` file in the backend directory (optional for basic functionality):

```env
# Supabase configuration (optional)
SUPABASE_URL=your_supabase_url_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
SUPABASE_ANON_KEY=your_anon_key_here

# Database configuration (optional)
DATABASE_URL=postgresql://username:password@host:port/database_name
```

### Frontend Environment Variables

Create a `.env` file in the frontend directory (optional):

```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=MLB Props Predictor
```

## Development

### Running Both Services

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Current Features Working

✅ **Live Data Integration**
- DraftKings API integration
- MLB statistics via pybaseball
- Real-time data processing

✅ **Full-Stack Application**
- React frontend with routing
- FastAPI backend with multiple endpoints
- Cross-origin resource sharing (CORS) configured

✅ **Modern UI/UX**
- Responsive design with Tailwind CSS
- Glass morphism effects
- Animated components
- Loading states and error handling

✅ **Betting Predictions**
- Player-specific prop predictions
- Confidence scoring system
- Visual confidence indicators
- Formatted betting data presentation

## Next Steps

### Phase 1: Data Enhancement
- [ ] Complete betting data mapping (team, position, specific bets)
- [ ] Implement confidence calculation algorithms
- [ ] Add more comprehensive player statistics
- [ ] Integrate injury reports and lineup data

### Phase 2: Machine Learning Integration
- [ ] Develop prediction models for player performance
- [ ] Implement historical performance analysis
- [ ] Add statistical trend analysis
- [ ] Create confidence scoring based on historical accuracy

### Phase 3: User Experience
- [ ] Add user authentication system
- [ ] Implement prediction tracking
- [ ] Create personalized dashboards
- [ ] Add notification system for high-confidence bets

### Phase 4: Advanced Features
- [ ] Real-time game updates
- [ ] Social features (sharing predictions)
- [ ] Mobile application
- [ ] Premium subscription features

### Phase 5: Production Deployment
- [ ] Comprehensive testing suite
- [ ] Performance optimization
- [ ] Security hardening
- [ ] CI/CD pipeline setup
- [ ] Docker containerization

## Troubleshooting

### Common Issues

**Backend Issues:**
- **pybaseball rate limiting**: Add delays between requests
- **DraftKings API changes**: Check headers and URL endpoints
- **Python version compatibility**: Ensure Python 3.8+ is installed

**Frontend Issues:**
- **CORS errors**: Ensure backend is running on port 8000
- **API connection**: Check backend server status
- **Build errors**: Clear node_modules and reinstall dependencies

**Data Issues:**
- **Missing statistics**: pybaseball requires internet connection
- **Outdated odds**: DraftKings API data may be cached
- **Empty results**: Check API response format and error handling

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 