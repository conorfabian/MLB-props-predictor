import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from helpers import get_bets
from database import store_bets
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BetScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        self.setup_jobs()
    
    def setup_jobs(self):
        self.scheduler.add_job(
            self.fetch_and_store_bets,
            CronTrigger(minute=0),
            id='fetch_bets_hourly',
            name='Fetch and store bets every hour',
            replace_existing=True
        )
        
        self.scheduler.add_job(
            self.fetch_and_store_bets,
            'date',
            run_date=datetime.now(),
            id='fetch_bets_startup',
            name='Fetch bets on startup'
        )
    
    async def fetch_and_store_bets(self):
        try:
            logger.info("Starting scheduled bet fetch...")
            bets_data = get_bets()
            
            if bets_data and bets_data.get("data"):
                success = store_bets(bets_data["data"])
                if success:
                    logger.info(f"Successfully stored {len(bets_data['data'])} bets")
                else:
                    logger.error("Failed to store bets in database")
            else:
                logger.warning("No betting data received from API")
                
        except Exception as e:
            logger.error(f"Error in scheduled bet fetch: {e}")
    
    def start(self):
        self.scheduler.start()
        logger.info("Bet scheduler started")
    
    def shutdown(self):
        self.scheduler.shutdown()
        logger.info("Bet scheduler stopped")

bet_scheduler = BetScheduler() 