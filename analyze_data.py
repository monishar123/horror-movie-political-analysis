import pandas as pd
import matplotlib.pyplot as plt

# Load the movies data directly (no need to access 'results' key)
file = 'movies.json'
movies_df = pd.read_json(file)

# Check the JSON structure by printing out the first few rows
print("JSON File Content:")
print(movies_df.head())

# Ensure 'release_date' is a datetime object
if 'release_date' in movies_df.columns:
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
    print("\nAfter converting 'release_date' to datetime:")
    print(movies_df['release_date'].head())
else:
    print("Error: 'release_date' column is missing.")

# Now calculate the number of movies per year
if 'release_date' in movies_df.columns:
    movies_by_year = movies_df['release_date'].dt.year.value_counts().sort_index()

    # Print movies by year
    print("\nMovies by Year:")
    print(movies_by_year)

    # Plot movies by year
    plt.figure(figsize=(10, 6))
    movies_by_year.plot(kind='line', marker='o')
    plt.title("Number of Movies by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.grid(True)
    plt.show()
else:
    print("Error: 'release_date' is missing or invalid.")

# Loading political events data for plotting the political crises
political_file = 'political_events.csv'  # Path to the political events file
events_df = pd.read_csv(political_file)

# Clean up column names (remove leading/trailing spaces)
events_df.columns = events_df.columns.str.strip()

# Print the columns of the political events dataset
print("\nColumns in Political Events Data:")
print(events_df.columns)

# Check the first few rows to ensure 'Type of Crisis' exists and contains data
print("\nFirst few rows of political events data:")
print(events_df.head())

# Check if 'Type of Crisis' exists in the columns
if 'Type of Crisis' in events_df.columns:
    # Count the occurrences of each crisis type
    crisis_counts = events_df['Type of Crisis'].value_counts()

    # Print the crisis counts
    print("\nPolitical Events by Type:")
    print(crisis_counts)

    # Plot the political events by type
    plt.figure(figsize=(14, 7))
    crisis_counts.plot(kind='bar', color='lightblue')
    plt.title("Political Events by Crisis Type")
    plt.xlabel("Type of Crisis")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.tight_layout()  # To prevent cut-off labels
    plt.show()
else:
    print("Error: 'Type of Crisis' column is missing.")

