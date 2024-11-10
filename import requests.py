
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of the website you want to scrape
url = "https://www.imdb.com/search/title/?genres=horror"  # Replace with the actual URL

# Step 2: Send a GET request to the website
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 5: Extract movie data
    movies = []
    for movie in soup.find_all('div', class_='lister-item mode-advanced'):  # Adjust the class name as needed
        title = movie.h3.a.text  # Extracting the title
        year = movie.h3.find('span', class_='lister-item-year').text  # Extracting the year
        movies.append({'Title': title, 'Year': year})

    # Step 6: Create a DataFrame and save to CSV
    df = pd.DataFrame(movies)
    df.to_csv('movies.csv', index=False)
    print("Data saved to movies.csv")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)