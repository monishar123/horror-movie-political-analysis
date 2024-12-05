import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
url = "https://api.themoviedb.org/3/movie/popular"

params = {
    "api_key": API_KEY,  # Include the API key here
    "language": "en-US",
    "page": 1
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    print("Data retrieved successfully:", data)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)