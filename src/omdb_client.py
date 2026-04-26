import requests
from config import API_KEY

def get_movie_data(title, year, api_key=API_KEY):
    url = f'http://www.omdbapi.com/'  
    parameters = {
        't': title,
        'y': year,
        'apikey': api_key
    }
    try:
        response = requests.get(url, params=parameters, timeout=4)
        response.raise_for_status()
        data = response.json()
        
        if data.get("Response") == "False":
            print(f"❌ Not found: {title} ({year}) — {data.get('Error')}")
            return None
        
        print(f"✅ Enriched: {title} ({year})")
        
        return {
            "imdb_rating": data.get("imdbRating", "N/A"),
            "actors": data.get("Actors", "N/A"),
            "imdb_votes": data.get("imdbVotes", "N/A")
        }
    
    except requests.exceptions.Timeout:
        print(f"❌ Timeout: {title} ({year})")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {title} ({year}): {e}")
        return None
    