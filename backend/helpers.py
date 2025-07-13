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
    raw = live_bets()
    if not raw:
        return {"message": "Unable to fetch current betting data", "data": []}
    
    bets = []
    for i, sel in enumerate(raw[:5]):
        name = sel["playerName"]
        meta = get_player_meta(name)

        bets.append({
            "id": i + 1,
            "playerName": name,
            "team": meta["team"] or "Unknown",
            "position": meta["position"] or "Unknown",
            "photo": meta["photo"],
            "bet": sel["milestone"],
            "odds": sel["oddsAmerican"],
            "confidence": 89,
            "description": "Description",
            "reasoning": "Reasoning"
        })

    return {"message": "Live betting data from DraftKings", "data": bets}