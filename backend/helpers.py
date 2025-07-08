from pybaseball import pitching_stats_bref, cache
import time
import requests

url = "https://sportsbook-nash.draftkings.com/api/sportscontent/dkusnj/v1/leagues/84240/categories/743/subcategories/17319"
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
    return data