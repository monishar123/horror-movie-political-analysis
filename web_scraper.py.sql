import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Specify the URL
url = 'https://example.com/movies'  # Replace with your target URL

# Step 2: Send a GET request to the URL
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 5: Extract movie details
    movies = []
    for movie in soup.find_all('div', class_='movie'):  # Update the class name based on the actual structure
        title = movie.find('h2').text  # Assuming titles are in <h2> tags
        year = movie.find('span', class_='year').text  # Assuming years are in <span> with class 'year'
        movies.append({'Title': title, 'Year': year})

    # Step 6: Create a DataFrame and save to CSV
    df = pd.DataFrame(movies)
    df.to_csv('movies.csv', index=False)
    print("Data saved to movies.csv")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


