from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests
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
                "player": "Aaron Judge",
                "team": "NYY",
                "prop_type": "home_runs",
                "line": 0.5,
                "prediction": "over"
            },
            {
                "id": 2,
                "player": "Mookie Betts",
                "team": "LAD",
                "prop_type": "hits",
                "line": 1.5,
                "prediction": "under"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)