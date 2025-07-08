from pybaseball import pitching_stats_bref, cache
import pandas as pd
import time
import requests

url = "https://sportsbook-nash.draftkings.com/api/sportscontent/dkusnj/v1/leagues/84240/categories/743/subcategories/17844"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://sportsbook.draftkings.com",
    "Referer": "https://sportsbook.draftkings.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

def pitching_stats(year):
    try:
        # Use Baseball Reference function (avoids FanGraphs 403 errors)
        # Add a small delay to avoid rate limiting
        time.sleep(0.5)
        
        # Get data for 2014 season (pitching_stats_bref only takes one season at a time)
        print("Fetching pitching data...")
        data = pitching_stats_bref(year)
        print(f"Retrieved {len(data)} pitching records for 2014")
        
        # Return basic stats info instead of full dataset (for testing)
        return {
            "success": True,
            "message": "Successfully retrieved pitching stats",
            "count": len(data),
            "season": year,
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
    
def sports_data():
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

def sports_bets():
    data = sports_data()

    if not data:
        return {
            "message": "Unable to fetch current betting data",
            "data": []
        }
    
    bets = []
    for i, bet in enumerate(data):
        bets.append({
            "id": i + 1,
            "playerName": bet.get("playerName", "Unknown Player"),
            "team": "TBD",
            "position": "TBD",
            "photo": f"https://via.placeholder.com/120x120/1e293b/ffffff?text={bet.get('playerName', 'Player')[:2].upper()}",
            "bet": "TBD",
            "odds": "TBD",
            "confidence": 89,
            "description": "TBD",
            "reasoning": "TBD"
        })
    
    return {
        "message": "Live betting data from DraftKings",
        "data": bets
    }