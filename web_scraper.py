import requests
from bs4 import BeautifulSoup

# URL of the horror movie list (replace with an actual URL)
url = "https://real-movie-data-source.com" # <-- Change this URL

# Make a request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract movie titles (modify this to match the actual HTML structure)
    movie_titles = soup.find_all('h2', class_='movie-title')  # <-- Adjust as needed
    for title in movie_titles:
        print(title.text)  # Print each movie title
else:
    print("Failed to retrieve the page.")
movie_titles = soup.find_all('h2', class_='movie-title')  # Adjust to real tags/classes
