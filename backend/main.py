from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from helpers import pitching_stats, sports_data

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Sports Bet API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic health check endpoint
@app.get("/")
async def root():
    return {"message": "MLB Props Predictor API is running"}

@app.get("/get-sports-data")
async def get_sports_data():
    return sports_data()

@app.get("/get-pitching-stats")
async def get_pitching_stats():
    return pitching_stats(2025)

# Placeholder endpoint for bets
@app.get("/api/bets")
async def get_bets():
    return {
        "message": "Bets endpoint placeholder",
        "data": [
            {
                "id": 1,
                "playerName": "Aaron Judge",
                "team": "NYY",
                "position": "OF",
                "photo": "https://via.placeholder.com/120x120/1e293b/ffffff?text=AJ",
                "bet": "Over 1.5 Total Bases",
                "odds": "+110",
                "confidence": 89,
                "description": "Judge has exceeded 1.5 total bases in 8 of his last 10 games. Facing a left-handed pitcher with a 5.2 ERA against righties this season.",
                "reasoning": "Strong recent form, favorable matchup vs LHP, excellent home stats"
            },
            {
                "id": 2,
                "playerName": "Ronald Acuña Jr.",
                "team": "ATL",
                "position": "OF",
                "photo": "https://via.placeholder.com/120x120/1e293b/ffffff?text=RA",
                "bet": "Over 0.5 Stolen Bases",
                "odds": "+120",
                "confidence": 78,
                "description": "Acuña has stolen 1.5 bases in 6 of his last 10 games. Facing a right-handed pitcher with a 4.5 ERA against lefties this season.",
                "reasoning": "Strong recent form, favorable matchup vs RHP, good stolen base stats"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)