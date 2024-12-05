import json

# Load the JSON file
with open("movies.json", "r") as file:
    data = json.load(file)

# Print the content to verify
print(json.dumps(data, indent=4))
