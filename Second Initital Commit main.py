
import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikimedia page you'd like to scrape
url = "https://en.wikipedia.org/wiki/List_of_political_crises"

# Send a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract information based on the HTML structure
# Adjust these selectors depending on the specific structure of the Wikimedia page

# Example: Finding all headers or crisis sections by tags, classes, or specific identifiers
crises = []
for section in soup.find_all('h2'):
    decade = section.get_text(strip=True)
    crisis_list = section.find_next_sibling('ul')  # Assuming crises are listed in an unordered list

    if crisis_list:
        for crisis in crisis_list.find_all('li'):
            crises.append({
                "decade": decade,
                "crisis": crisis.get_text(strip=True)
            })

# Optionally save