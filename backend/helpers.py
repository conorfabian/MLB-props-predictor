from pybaseball import playerid_lookup
from io import StringIO
import pandas as pd
import numpy as np
import time
import requests
import random

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

url = "https://api.prizepicks.com/projections?league_id=2"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
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
    url = "https://api.prizepicks.com/projections?league_id=2"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

    try:
        raw_data = response.json()
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return None

    projections = raw_data.get("data", [])
    included = raw_data.get("included", [])

    player_map = {}
    team_map = {}

    for item in included:
        if item["type"] == "new_player":
            player_map[item["id"]] = {
                "name": item["attributes"]["name"],
                "team_id": item["attributes"].get("team_id"),
                "position": item["attributes"].get("position")
            }
        elif item["type"] == "team":
            team_map[item["id"]] = item["attributes"]["name"]

    batters_odds = []
    for proj in projections:
        attr = proj["attributes"]
        rel = proj["relationships"]

        if attr.get("odds_type") != "standard":
            continue

        player_id = rel["new_player"]["data"]["id"]
        player = player_map.get(player_id, {})
        
        stat_type = attr.get("stat_type", "Unknown")
        line = attr.get("line_score")
        
        if line is not None:
            milestone = f"{stat_type} : {line}"
        else:
            milestone = stat_type

        odds_american = "+100"
        odds_decimal = 2.0

        batters_odds.append({
            "playerName": player.get("name", "Unknown"),
            "milestone": milestone,
            "oddsDecimal": odds_decimal,
            "oddsAmerican": odds_american
        })

    if not batters_odds:
        print("No valid projections found for batters.")
        return None

    return batters_odds

def get_bets():
    try:
        raw = live_bets()
        if not raw:
            logger.warning("No raw betting data received")
            return {"message": "Unable to fetch current betting data", "data": []}
        
        # Randomized descriptions and reasoning for MVP
        descriptions = [
            "Strong statistical model indicates favorable outcome",
            "Advanced analytics suggest high probability of success",
            "Player performance trends support this prediction",
            "Historical data patterns align with this projection",
            "Recent form and matchup analysis favor this bet",
            "Machine learning model indicates value in this line",
            "Statistical analysis reveals edge in this market",
            "Performance metrics suggest undervalued opportunity"
        ]
        
        reasonings = [
            "Based on advanced sabermetrics and recent performance trends",
            "Machine learning analysis of player splits and matchup data",
            "Historical performance patterns and current season metrics",
            "Statistical modeling incorporating weather and ballpark factors",
            "Advanced analytics considering opposing pitcher tendencies",
            "Performance regression analysis and situational statistics",
            "Data-driven model factoring in recent form and team dynamics",
            "Comprehensive statistical analysis of player consistency metrics"
        ]
        
        bets = []
        for i, sel in enumerate(raw[:9]):
            try:
                name = sel["playerName"]
                meta = get_player_meta(name)

                # Randomize confidence between 60-95
                confidence = random.randint(60, 95)
                
                # Randomly select description and reasoning
                description = random.choice(descriptions)
                reasoning = random.choice(reasonings)

                bets.append({
                    "id": i + 1,
                    "playerName": name,
                    "team": meta["team"] or "Unknown",
                    "position": meta["position"] or "Unknown",
                    "photo": meta["photo"],
                    "bet": sel["milestone"],
                    "odds": sel["oddsAmerican"],
                    "oddsDecimal": sel["oddsDecimal"],
                    "confidence": confidence,
                    "description": description,
                    "reasoning": reasoning
                })
            except Exception as e:
                logger.error(f"Error processing bet for {sel.get('playerName', 'unknown')}: {e}")
                continue

        logger.info(f"Successfully processed {len(bets)} bets")
        return {"message": "Live betting data processed", "data": bets}
        
    except Exception as e:
        logger.error(f"Error in get_bets: {e}")
        return {"message": "Error fetching betting data", "data": []}