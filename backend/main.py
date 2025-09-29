from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="MLB Props Predictor API", version="1.0.0")

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