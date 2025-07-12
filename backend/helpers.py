from pybaseball import pitching_stats_bref, cache
import pandas as pd
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