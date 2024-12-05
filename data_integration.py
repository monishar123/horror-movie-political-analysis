import pandas as pd
import json

# Load movie data
with open("movies.json", "r") as file:
    movies_data = json.load(file)
movies_df = pd.DataFrame(movies_data["results"])

# Load political event data
political_df = pd.read_excel("political_events.xlsx")  # Use read_csv if you converted it to CSV

# Example: Merge or analyze relationships
print("Movies Data:")
print(movies_df.head())
print("\nPolitical Events Data:")
print(political_df.head())
