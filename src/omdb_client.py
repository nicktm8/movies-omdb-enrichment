import requests
from config import API_KEY

def get_movie_data(title, year, api_key=API_KEY):
    url = f'http://www.omdbapi.com/'  
    parameters = {
        't': title,
        'y': year,
        'apikey': api_key
    }
    response = requests.get(url, params=parameters, timeout=4)
    
    print(f"❓ Requesting: {title} ({year})")
    
    if response.status_code == 200:
        data = response.json()
        return {
            "imdb_rating": data.get("imdbRating", "N/A"),
            "actors": data.get("Actors", "N/A"),
            "imdb_votes": data.get("imdbVotes", "N/A")
        }
        
    else:
        print(f"❌ Failed to fetch data for {title} ({year}): {response.status_code}")
        return None
