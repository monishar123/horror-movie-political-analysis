python fetch_imdb_data.py
import requests

# IMDb API endpoint (example)
url = "https://api.themoviedb.org/3/movie/popular"  # Replace with actual IMDb endpoint

# API headers with Authorization token
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NzM3MGYwMjFlMjllZjVkZmJkMmNiZjZiOGUxNTUxNiIsIm5iZiI6MTczMTI1MjMxMS45MDkzMjg3LCJzdWIiOiI2NzIyM2IzYmZlMmE4YTAxMWVkNzFhYjUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.i4SW4q-TOBM8uXTN3XR4ZsI92aHsp50CM-kMcMKKX2Q",
    "Content-Type": "application/json;charset=utf-8"
}

# Optional: Include additional parameters if needed by the endpoint
params = {
    "api_key": "47370f021e29ef5dfbd2cbf6b8e15516"
}

# Fetch data from IMDb API
try:
    response = requests.get(url, headers=headers, params=params)
    
    # Check for successful response
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        print("Data retrieved successfully:", data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print("Error message:", response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
