import requests

# Function to fetch political data from Wikimedia API
def fetch_political_data(query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={query}&utf8="
    
    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        print("Error fetching data:", data['error'])
        return []

    # Extract the titles of the search results
    search_results = [result['title'] for result in data['query']['search']]
    return search_results

# Function to fetch movies from a decade (using your movie scraper)
def fetch_movies_by_decade(decade_start, decade_end, API_KEY):
    BASE_URL = "https://api.themoviedb.org/3/discover/movie"
    url = f"{BASE_URL}?api_key={API_KEY}&with_genres=27&primary_release_date.gte={decade_start}-01-01&primary_release_date.lte={decade_end}-12-31"
    response = requests.get(url)
    data = response.json()
    return data.get('results', [])

# Example usage: Fetch political events or crises
political_events = fetch_political_data("political crises")
print("Political events or crises found:", political_events)

# Example usage: Fetch horror movies from the 1980s
API_KEY = "your_api_key_here"  # Replace with your actual TMDB API Key
movies_1980s = fetch_movies_by_decade("1980", "1989", API_KEY)
for movie in movies_1980s:
    print(movie['title'])
