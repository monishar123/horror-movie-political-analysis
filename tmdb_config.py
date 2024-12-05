import requests
from tmdb_config import TMDB_API_KEY

# Example function to get movie details using the TMDB API
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
movie_data = get_movie_details(550)  # Example movie ID (Fight Club)
if movie_data:
    print(movie_data)
else:
    print("Failed to fetch movie details.")
