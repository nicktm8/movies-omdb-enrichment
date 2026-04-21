import requests
from config import API_KEY

def get_movie_data(title, year, api_key=API_KEY):
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={title}&y={year}'  
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Failed to fetch data for {title} ({year}): {response.status_code}")
        return None
