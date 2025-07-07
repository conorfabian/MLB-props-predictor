from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pybaseball import pitching_stats_bref, cache
import pandas as pd
import os
import requests
import httpx
import time

# Load environment variables
load_dotenv()

# Enable pybaseball caching to avoid repeated requests
cache.enable()

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
    try:
        # Use Baseball Reference function (avoids FanGraphs 403 errors)
        # Add a small delay to avoid rate limiting
        time.sleep(0.5)
        
        # Get data for 2014 season (pitching_stats_bref only takes one season at a time)
        print("Fetching pitching data...")
        data = pitching_stats_bref(2014)
        print(f"Retrieved {len(data)} pitching records for 2014")
        
        # Return basic stats info instead of full dataset (for testing)
        return {
            "success": True,
            "message": "Successfully retrieved pitching stats",
            "count": len(data),
            "season": 2014,
            "columns": list(data.columns),
            "sample_player": data.iloc[0]['Name'] if len(data) > 0 else None
        }
    except Exception as e:
        print(f"Error fetching pitching stats: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to fetch pitching stats. The data source might be temporarily unavailable."
        }

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