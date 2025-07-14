import os
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import List, Dict, Optional
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

def get_supabase_client() -> Client:
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise ValueError("Supabase credentials not found in environment variables")
    
    try:
        supabase: Client = create_client(
            supabase_url=SUPABASE_URL, 
            supabase_key=SUPABASE_SERVICE_ROLE_KEY
        )
        return supabase
    except Exception as e:
        logger.error(f"Failed to create Supabase client: {e}")
        raise

def store_bets(bets_data: List[Dict]) -> bool:
    try:
        supabase = get_supabase_client()
        
        supabase.table("bets").update({"is_active": False}).eq("is_active", True).execute()
        
        formatted_bets = []
        for bet in bets_data:
            formatted_bets.append({
                "player_name": bet["playerName"],
                "team": bet["team"],
                "position": bet["position"],
                "photo_url": bet["photo"],
                "bet_description": bet["bet"],
                "odds": bet["odds"],
                "confidence": bet["confidence"],
                "reasoning": bet["reasoning"],
                "is_active": True
            })
        
        result = supabase.table("bets").insert(formatted_bets).execute()
        
        logger.info(f"Successfully stored {len(formatted_bets)} bets")
        return True
        
    except Exception as e:
        logger.error(f"Error storing bets: {e}")
        return False

def get_active_bets() -> List[Dict]:
    try:
        supabase = get_supabase_client()
        
        result = supabase.table("bets").select("*").eq("is_active", True).order("created_at", desc=True).execute()
        
        formatted_bets = []
        for i, bet in enumerate(result.data):
            formatted_bets.append({
                "id": bet["id"],
                "playerName": bet["player_name"],
                "team": bet["team"],
                "position": bet["position"],
                "photo": bet["photo_url"],
                "bet": bet["bet_description"],
                "odds": bet["odds"],
                "confidence": bet["confidence"],
                "reasoning": bet["reasoning"],
                "createdAt": bet["created_at"]
            })
        
        return formatted_bets
        
    except Exception as e:
        logger.error(f"Error retrieving bets: {e}")
        return []

def get_bet_history(limit: int = 100) -> List[Dict]:
    try:
        supabase = get_supabase_client()
        
        result = supabase.table("bets").select("*").order("created_at", desc=True).limit(limit).execute()
        
        return result.data
        
    except Exception as e:
        logger.error(f"Error retrieving bet history: {e}")
        return [] 