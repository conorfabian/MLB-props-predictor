from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pybaseball import pitching_stats
import pandas as pd
import os
import requests
import httpx

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

url = "https://sportsbook-nash.draftkings.com/api/sportscontent/dkusnj/v1/leagues/84240/categories/743/subcategories/17319"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://sportsbook.draftkings.com",
    "Referer": "https://sportsbook.draftkings.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

# Basic health check endpoint
@app.get("/")
async def root():
    return {"message": "MLB Props Predictor API is running"}

@app.get("/get-sports-data")
async def get_sports_data():
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

@app.get("/get-pitching-stats")
async def get_pitching_stats():
    stats_df = pitching_stats(2024)
    stats_df = stats_df.where(pd.notnull(stats_df), None)  # Convert NaN to None
    return stats_df.to_dict(orient="records")

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