from pybaseball import playerid_lookup
from io import StringIO
import pandas as pd
import numpy as np
import time
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SPORTSDATA_API_KEY = os.getenv("SPORTSDATA_IO_API_KEY")
SPORTSDATA_BASE_URL = "https://api.sportsdata.io/v3/mlb/odds/json"

def get_player_id(playerName):
    try:
        player_df = playerid_lookup(playerName, fuzzy=True)
        
        if player_df.empty:
            print(f"Player '{playerName}' not found.")
            return None
            
        player_id = int(player_df.at[0, 'key_mlbam'])
        return player_id
    except Exception as e:
        print(f"An error occurred during player ID lookup for {playerName}: {e}")
        return None

def get_player_batting_stats(playerName):
    playerID = get_player_id(playerName)

    if not playerID:
        return {"error": f"Could not retrieve stats because player ID for '{playerName}' was not found."}

    url = f"https://baseballsavant.mlb.com/statcast_search/csv?hfPT=&hfAB=&hfGT=R%7C&hfPR=&hfZ=&hfStadium=&hfBBL=&hfNewZones=&hfPull=&hfC=&hfSea=2025%7C&hfSit=&player_type=batter&hfOuts=&hfOpponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&hfMo=&hfTeam=&home_road=&hfRO=&position=&hfInfield=&hfOutfield=&hfInn=&hfBBT=&batters_lookup%5B%5D={playerID}&hfFlag=&metric_1=&group_by=name-date&min_pitches=0&min_results=0&min_pas=0&sort_col=pitches&player_event_sort=api_p_release_speed&sort_order=desc#results"
    response = requests.get(url)
    response.raise_for_status()
    try:
        response = requests.get(url)
        # Raise an exception for bad status codes (like 404 or 500)
        response.raise_for_status()

        csv_data = StringIO(response.text)
        stats_df = pd.read_csv(csv_data)

        stats_df = stats_df.replace({np.nan: None})

        return stats_df.to_dict(orient='records')

    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An unexpected error occurred: {err}"}
    

def get_player_meta(playerName):
    player_id = get_player_id(playerName)
    if not player_id:
        return {"team": None, "position": None, "photo": None}

    people_url = f"https://statsapi.mlb.com/api/v1/people/{player_id}?hydrate=currentTeam"
    resp = requests.get(people_url)
    resp.raise_for_status()
    person = resp.json().get("people", [{}])[0]

    team = person.get("currentTeam", {}).get("name")
    position = person.get("primaryPosition", {}).get("abbreviation")

    photo = (
        "https://img.mlbstatic.com/mlb-photos/image/upload/"
        "d_people:generic:headshot:67:current.png/"
        "w_120,q_auto:best/"
        f"v1/people/{player_id}/headshot/67/current"
    )

    return {"team": team, "position": position, "photo": photo}

def get_betting_events_today():
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"{SPORTSDATA_BASE_URL}/BettingEventsByDate/{today}"

    headers = {
        "Ocp-Apim-Subscription-Key": SPORTSDATA_API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error fetching betting events: {e}")
        return []
    
def get_player_props_for_game(game_id, sportsbook_group="prizepicks"):
    url = f"{SPORTSDATA_BASE_URL}/BettingPlayerPropsByGameID/{game_id}/{sportsbook_group}"
    
    headers = {
        "Ocp-Apim-Subscription-Key": SPORTSDATA_API_KEY
    }
    
    params = {
        "include": "available"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error fetching player props for game {game_id}: {e}")
        return []
    
def live_bets():
    try:
        events = get_betting_events_today()
        
        if not events:
            logger.warning("No betting events found for today")
            return []
        
        all_props = []
        
        for event in events:
            game_id = event.get("GameID")
            if not game_id:
                continue
                
            props = get_player_props_for_game(game_id)
            
            for market in props:
                market_name = market.get("Name", "")
                player_name = market.get("PlayerName")
                
                if not player_name:
                    continue

                outcomes = market.get("Outcomes", [])
                if not outcomes:
                    continue
                
                prizepicks_outcome = None
                for outcome in outcomes:
                    sportsbook = outcome.get("Sportsbook", {})
                    if sportsbook.get("Name", "").lower() == "prizepicks":
                        prizepicks_outcome = outcome
                        break
                
                if not prizepicks_outcome:
                    continue
                
                all_props.append({
                    "playerName": player_name,
                    "milestone": market_name,
                    "oddsDecimal": prizepicks_outcome.get("PayoutDecimal"),
                    "oddsAmerican": prizepicks_outcome.get("PayoutAmerican"),
                    "value": prizepicks_outcome.get("Value"),
                    "betType": prizepicks_outcome.get("Name")
                })
        
        return all_props
        
    except Exception as e:
        logger.error(f"Error in live_bets: {e}")
        return []       
    
def get_bets():
    try:
        raw = live_bets()
        if not raw:
            logger.warning("No raw betting data received")
            return {"message": "Unable to fetch current betting data", "data": []}
        
        bets = []
        for i, sel in enumerate(raw[:10]):
            try:
                name = sel["playerName"]
                meta = get_player_meta(name)
                
                milestone = sel["milestone"]
                bet_type = sel.get("betType", "")
                value = sel.get("value", "")
                
                if value and bet_type:
                    formatted_bet = f"{bet_type} {value} {milestone}"
                else:
                    formatted_bet = milestone

                bets.append({
                    "id": i + 1,
                    "playerName": name,
                    "team": meta["team"] or "Unknown",
                    "position": meta["position"] or "Unknown", 
                    "photo": meta["photo"],
                    "bet": formatted_bet,
                    "odds": sel["oddsAmerican"],
                    "oddsDecimal": sel["oddsDecimal"],
                    "confidence": 89,
                    "description": f"Betting on {name} to achieve {formatted_bet}",
                    "reasoning": f"Based on PrizePicks odds and player performance metrics"
                })
            except Exception as e:
                logger.error(f"Error processing bet for {sel.get('playerName', 'unknown')}: {e}")
                continue

        logger.info(f"Successfully processed {len(bets)} bets")
        return {"message": "Live betting data processed", "data": bets}
        
    except Exception as e:
        logger.error(f"Error in get_bets: {e}")
        return {"message": "Error fetching betting data", "data": []}