from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from contextlib import asynccontextmanager
import logging
from database import get_active_bets, get_bet_history
from scheduler import bet_scheduler

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up MLB Props Predictor API...")
    bet_scheduler.start()
    yield
    logger.info("Shutting down MLB Props Predictor API...")
    bet_scheduler.shutdown()

app = FastAPI(
    title="MLB Props Predictor API", 
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mlb-props-predictor-*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MLB Props Predictor API is running"}

@app.get("/api/bets")
async def get_current_bets():
    try:
        bets = get_active_bets()
        return {
            "message": "Current active bets from database",
            "data": bets,
            "count": len(bets)
        }
    except Exception as e:
        logger.error(f"Error fetching bets: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch bets")

@app.get("/api/bets/history")
async def get_bets_history(limit: int = 100):
    try:
        history = get_bet_history(limit)
        return {
            "message": "Bet history from database",
            "data": history,
            "count": len(history)
        }
    except Exception as e:
        logger.error(f"Error fetching bet history: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch bet history")

@app.post("/api/bets/refresh")
async def manual_refresh():
    try:
        await bet_scheduler.fetch_and_store_bets()
        return {"message": "Bet refresh triggered successfully"}
    except Exception as e:
        logger.error(f"Error in manual refresh: {e}")
        raise HTTPException(status_code=500, detail="Failed to refresh bets")

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "scheduler_running": bet_scheduler.scheduler.running,
        "next_run": str(bet_scheduler.scheduler.get_jobs()[0].next_run_time) if bet_scheduler.scheduler.get_jobs() else None
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)