from pybaseball import playerid_lookup
from io import StringIO
import pandas as pd
import numpy as np
import time
import requests

url = "https://sportsbook-nash.draftkings.com/api/sportscontent/dkusnj/v1/leagues/84240/categories/743/subcategories/17320"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://sportsbook.draftkings.com",
    "Referer": "https://sportsbook.draftkings.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

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
    
def live_bets():
    response = requests.get(url, headers=headers)
    data = response.json()

    market_id = {}
    for market in data.get("markets", []):
        if market.get("name"):
            market_id[market.get("name")] = market.get("id")

    if not market_id:
        print("No markets found.")
        return None

    id_to_market = {v: k for k, v in market_id.items()}
    
    batters_odds = []
    for selection in data.get("selections", []):
        market_id_value = selection.get("marketId")
        if market_id_value in id_to_market:
            milestone = selection.get("label")
            odds = selection.get("displayOdds", {})
            odds_decimal = odds.get("decimal")
            odds_american = odds.get("american")
            
            batters_odds.append({
                "playerName": id_to_market[market_id_value],
                "milestone": milestone,
                "oddsDecimal": odds_decimal,
                "oddsAmerican": odds_american
            })

    if not batters_odds:
        print("No valid odds found for batters.")
        return None

    return batters_odds

def get_bets():
    data = live_bets()

    if not data:
        return {
            "message": "Unable to fetch current betting data",
            "data": []
        }
    
    bets = []
    count = 0
    for i, bet in enumerate(data):
        if count > 4:
            break
        count += 1
        bets.append({
            "id": i + 1,
            "playerName": bet.get("playerName", "Unknown Player"),
            "team": "TBD",
            "position": "TBD",
            "photo": f"https://via.placeholder.com/120x120/1e293b/ffffff?text={bet.get('playerName', 'Player')[:2].upper()}",
            "bet": bet.get("milestone"),
            "odds": bet.get("oddsAmerican"),
            "confidence": 89,
            "description": "TBD",
            "reasoning": "TBD"
        })
    
    return {
        "message": "Live betting data from DraftKings",
        "data": bets
    }