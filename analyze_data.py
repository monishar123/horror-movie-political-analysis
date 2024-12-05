import pandas as pd

# Load the movies data
movies_df = pd.read_json("movies.json")

# Load the political events data
political_df = pd.read_excel("Political Crises Decade.xlsx")

# Inspect the data
print("Movies Data:")
print(movies_df.head(), "\n")

print("Political Events Data:")
print(political_df.head(), "\n")

# Example Analysis
# Count the number of movies
print(f"Number of Movies: {len(movies_df)}")

# Count political events by type
print("Political Events by Type:")
print(political_df["Type of Crisis"].value_counts())
import pandas as pd

# Load data from the Excel file instead of CSV
political_df = pd.read_excel("Political Crises Decade.xlsx")

# Display the first few rows of the data
print(political_df.head())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
movies_df = pd.read_json("movies.json")
political_df = pd.read_csv("political_events.csv")

# Political Events by Type of Crisis
political_type_counts = political_df["Type of Crisis"].value_counts()

# Bar chart with matplotlib
plt.figure(figsize=(12, 6))
political_type_counts.plot(kind="bar", color="skyblue")
plt.title("Political Events by Type")
plt.xlabel("Type of Crisis")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("political_events_chart.png")  # Save chart as an image
plt.show()

# Line chart for movies released over time
movies_df["release_date"] = pd.to_datetime(movies_df["release_date"])
movies_by_year = movies_df["release_date"].dt.year.value_counts().sort_index()

plt.figure(figsize=(12, 6))
movies_by_year.plot(kind="line", marker="o", color="orange")
plt.title("Movies Released Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_released_chart.png")  # Save chart as an image
plt.show()
