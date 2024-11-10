import requests  # Ensure requests is imported if needed for API calls

# Define the fetch_imdb_data function
def fetch_imdb_data():
    # Example API endpoint; replace with the actual IMDb endpoint if different
    url = "https://api.themoviedb.org/3/movie/popular"
    
    # Authorization headers
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NzM3MGYwMjFlMjllZjVkZmJkMmNiZjZiOGUxNTUxNiIsIm5iZiI6MTczMTI1MjMxMS45MDkzMjg3LCJzdWIiOiI2NzIyM2IzYmZlMmE4YTAxMWVkNzFhYjUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.i4SW4q-TOBM8uXTN3XR4ZsI92aHsp50CM-kMcMKKX2Q",
        "Content-Type": "application/json;charset=utf-8"
    }

    # Making the GET request
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            print("Data retrieved successfully:", data)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            print("Error message:", response.text)
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# Call the fetch_imdb_data function
fetch_imdb_data()