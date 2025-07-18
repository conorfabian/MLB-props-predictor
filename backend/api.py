import requests
from pprint import pprint

def fetch_mlb_projections():
    url = "https://api.prizepicks.com/projections?league_id=2"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print("Response text:", response.text[:300])
        return []

    try:
        raw_data = response.json()
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        print("Raw response text:", response.text[:300])
        return []

    projections = raw_data.get("data", [])
    included = raw_data.get("included", [])

    # Build lookup maps
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

    # Combine data
    props = []

    for proj in projections:
        attr = proj["attributes"]
        rel = proj["relationships"]

        player_id = rel["new_player"]["data"]["id"]
        player = player_map.get(player_id, {})
        team_id = player.get("team_id")
        team_name = team_map.get(str(team_id), "Unknown") if team_id else "Unknown"


        prop = {
            "name": player.get("name"),
            "team": team_name,
            "position": player.get("position"),
            "stat_type": attr.get("stat_type"),
            "line": attr.get("line_score"),
            "odds_type": attr.get("odds_type"),
            "start_time": attr.get("start_time")
        }
        props.append(prop)

    return props

if __name__ == "__main__":
    props = fetch_mlb_projections()
    for prop in props[:10000]:
        pprint(prop)