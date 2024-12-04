import requests
from dotenv import load_dotenv
import os

# Load API key and token from .env file
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BEARER_TOKEN = os.getenv("TMDB_BEARER_TOKEN")

# IMDb API endpoint (example)
url = "https://api.themoviedb.org/3/movie/popular"

# API headers with Authorization token
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

def fetch_data():
    """Fetch data from IMDb API and handle the response."""
    try:
        # Optional: Include additional parameters if needed by the endpoint
        params = {
            "api_key": API_KEY
        }

        # Fetch data from IMDb API
        response = requests.get(url, headers=headers, params=params)

        # Check for successful response
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            print("Data retrieved successfully!")
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            print("Error message:", response.text)
            return None

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    # Call fetch_data function
    data = fetch_data()
    if data:
        print("Retrieved Data:", data)
