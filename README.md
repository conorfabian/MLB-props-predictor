# MLB Props Predictor

A full-stack web application for predicting MLB player props using modern web technologies.

## Project Overview

This application consists of two main components:
- **Frontend**: React application with Vite and Tailwind CSS
- **Backend**: FastAPI application with Supabase/PostgreSQL database

## Current Status

✅ **Project is fully functional and ready for development**

Both frontend and backend are running successfully with all initial setup complete:
- Frontend: React + Vite + Tailwind CSS (http://localhost:5173)
- Backend: FastAPI + Uvicorn + CORS (http://localhost:8000)
- Database: Supabase integration configured
- API: Placeholder endpoints with sample MLB data

## Technology Stack

### Frontend
- **React 18** - Modern React with hooks
- **Vite** - Fast build tool and development server
- **Tailwind CSS** - Utility-first CSS framework
- **PostCSS** - CSS processing with autoprefixer

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for running FastAPI
- **Supabase** - Backend-as-a-Service with PostgreSQL database
- **python-dotenv** - Environment variable management
- **CORS** - Cross-Origin Resource Sharing configured

### Database
- **Supabase** - Hosted PostgreSQL with real-time capabilities
- **PostgreSQL** - Relational database for storing player stats and predictions

## Recent Fixes & Updates

### Frontend Fixes
- ✅ **Tailwind CSS PostCSS Plugin**: Updated to use `@tailwindcss/postcss` package
- ✅ **Configuration**: Fixed PostCSS configuration for proper Tailwind integration
- ✅ **Dependencies**: All frontend dependencies installed and working

### Backend Fixes
- ✅ **Python 3.13 Compatibility**: Removed `asyncpg` dependency (incompatible with Python 3.13)
- ✅ **Supabase Integration**: Using Supabase client directly for database operations
- ✅ **Virtual Environment**: Set up isolated Python environment
- ✅ **CORS Configuration**: Properly configured for React development server

## Quick Start

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8 or higher
- npm or yarn package manager
- pip package manager

### 1. Clone and Setup

```bash
git clone <repository-url>
cd mlb-props-predictor
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env.example .env
# Edit .env with your Supabase credentials

# Run the backend server
python main.py
```

Backend will be available at `http://localhost:8000`

### 3. Frontend Setup

```bash
# Navigate to frontend directory (in a new terminal)
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

Frontend will be available at `http://localhost:5173`

## Project Structure

```
mlb-props-predictor/
├── .gitignore              # Git ignore patterns
├── README.md               # This file
├── frontend/               # React frontend application
│   ├── src/               # Source code
│   │   ├── App.jsx        # Main app component
│   │   ├── index.css      # Tailwind CSS styles
│   │   └── main.jsx       # Entry point
│   ├── public/            # Static assets
│   ├── index.html         # HTML template
│   ├── package.json       # Frontend dependencies
│   ├── tailwind.config.js # Tailwind CSS configuration
│   ├── postcss.config.js  # PostCSS configuration
│   ├── vite.config.js     # Vite configuration
│   └── README.md          # Frontend documentation
└── backend/               # FastAPI backend application
    ├── main.py            # FastAPI application entry point
    ├── database.py        # Database connection setup
    ├── requirements.txt   # Python dependencies
    ├── env.example        # Environment variables template
    ├── venv/             # Virtual environment (created locally)
    └── README.md         # Backend documentation
```

## API Endpoints

### Current Endpoints (Working)
- `GET /` - Health check endpoint
  ```json
  {"message": "MLB Props Predictor API is running"}
  ```

- `GET /api/bets` - Get MLB betting predictions (placeholder data)
  ```json
  {
    "message": "Bets endpoint placeholder",
    "data": [
      {
        "id": 1,
        "player": "Aaron Judge",
        "team": "NYY",
        "prop_type": "home_runs",
        "line": 0.5,
        "prediction": "over"
      }
    ]
  }
  ```

### API Documentation
Once the backend is running, you can access:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Development

### Running Both Services

You'll need two terminal windows:

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # If using virtual environment
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Development Workflow

1. **Backend Development**: Modify Python files in `backend/`
2. **Frontend Development**: Modify React components in `frontend/src/`
3. **Database**: Configure Supabase connection in `backend/.env`
4. **Styling**: Use Tailwind CSS classes in React components
5. **API Integration**: Frontend can call backend endpoints

## Environment Setup

### Backend Environment Variables

Create a `.env` file in the backend directory:

```env
# Supabase configuration
SUPABASE_URL=your_supabase_url_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
SUPABASE_ANON_KEY=your_anon_key_here

# Database configuration
DATABASE_URL=postgresql://username:password@host:port/database_name

# App configuration
DEBUG=True
SECRET_KEY=your_secret_key_here
```

### Frontend Environment Variables (Optional)

Create a `.env` file in the frontend directory for any frontend-specific variables:

```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=MLB Props Predictor
```

## Dependencies

### Backend Dependencies (requirements.txt)
- `fastapi==0.104.1` - Web framework
- `uvicorn[standard]==0.24.0` - ASGI server
- `python-dotenv==1.0.0` - Environment variables
- `python-multipart==0.0.6` - File uploads
- `supabase==2.3.0` - Database client

### Frontend Dependencies (package.json)
- `react` - Frontend framework
- `vite` - Build tool
- `tailwindcss` - CSS framework
- `@tailwindcss/postcss` - PostCSS plugin
- `autoprefixer` - CSS vendor prefixes

## Next Steps

This is a boilerplate setup ready for development. Planned features include:

### Phase 1: Core Features
- [ ] Database schema design for player stats
- [ ] User authentication system
- [ ] Basic player statistics display
- [ ] Simple prediction interface

### Phase 2: Data Integration
- [ ] MLB API integration for real-time data
- [ ] Player statistics historical data
- [ ] Game schedules and results
- [ ] Betting odds integration

### Phase 3: Machine Learning
- [ ] Prediction models for player performance
- [ ] Historical performance analysis
- [ ] Trend analysis and insights
- [ ] Confidence scoring for predictions

### Phase 4: Advanced Features
- [ ] User profiles and preferences
- [ ] Prediction tracking and accuracy
- [ ] Social features (sharing predictions)
- [ ] Mobile responsiveness improvements

### Phase 5: Production
- [ ] Testing suite (unit, integration, e2e)
- [ ] Performance optimization
- [ ] Security hardening
- [ ] Deployment configuration (Docker, CI/CD)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Frontend won't start:**
- Check if Node.js is installed: `node --version`
- Reinstall dependencies: `cd frontend && npm install`

**Backend won't start:**
- Check if Python virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

**API calls failing:**
- Ensure backend is running on port 8000
- Check CORS configuration in `backend/main.py`
- Verify API endpoints in browser: `http://localhost:8000/docs`

**Database connection issues:**
- Verify Supabase credentials in `.env` file
- Check Supabase project status
- Test connection with `database.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please open an issue in the GitHub repository. 