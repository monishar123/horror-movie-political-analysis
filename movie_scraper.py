import os
import requests
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Access the API key from the .env file
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

# Function to fetch movies within a specified decade
def fetch_movies_by_decade(decade_start, decade_end):
    url = f"{BASE_URL}?api_key={API_KEY}&with_genres=27&primary_release_date.gte={decade_start}-01-01&primary_release_date.lte={decade_end}-12-31"
    response = requests.get(url)
    data = response.json()
    return data.get('results', [])

# Define the decades you want to fetch
decades = {
    "1960s": ("1960", "1969"),
    "1970s": ("1970", "1979"),
    "1980s": ("1980", "1989"),
    "1990s": ("1990", "1999"),
    "2000s": ("2000", "2009"),
    "2010s": ("2010", "2019"),
}

# Dictionary to store movies by decade
movies_by_decade = {}

# Loop through each decade, fetch movies, and store them
for decade, (start, end) in decades.items():
    print(f"Fetching horror movies from the {decade}...")
    movies = fetch_movies_by_decade(start, end)
    movies_by_decade[decade] = movies
    # Print the titles of movies for each decade
    for movie in movies:
        print(movie['title'])

# Optional: print summary
print("\nSummary of fetched movies by decade:")
for decade, movies in movies_by_decade.items():
    print(f"{decade}: {len(movies)} movies")

print(f"Using API Key: {API_KEY}")



