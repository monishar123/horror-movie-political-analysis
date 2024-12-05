import pandas as pd
import matplotlib.pyplot as plt

# Load the political events data
political_file = 'political_events.csv'
events_df = pd.read_csv(political_file)

# Clean up column names (remove leading/trailing spaces)
events_df.columns = events_df.columns.str.strip()

# Print the columns of the political events dataset
print("Columns in Political Events Data:")
print(events_df.columns)

# Check the first few rows to ensure 'Type of Crisis' exists and contains data
print("\nFirst few rows of political events data:")
print(events_df.head())

# Load the movies data
movies_df = pd.read_json('movies.json')

# Convert 'release_date' to datetime and extract the year
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
movies_df['release_year'] = movies_df['release_date'].dt.year  # Extract year for merging

# Check the first few rows of the movies data
print("\nMovies Data Columns:")
print(movies_df.columns)

# Merge movie and event data on the year
merged_df = pd.merge(movies_df, events_df, left_on='release_year', right_on='Year', how='left')

# Check merged data
print("\nMerged DataFrame:")
print(merged_df.head())

# Option 1: Movies by Crisis Type and Year (Stacked Bar Chart)
movies_by_crisis_year = merged_df.groupby(['Type of Crisis', 'release_year'])['title'].count().unstack().fillna(0)

# Plotting Movies by Crisis Type and Year
plt.figure(figsize=(14, 7))
movies_by_crisis_year.plot(kind='bar', stacked=True)
plt.title("Movies by Crisis Type and Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.tight_layout()  # To avoid cut-off labels
plt.show()

# Option 2: Total Movies per Crisis Type (Bar Chart)
crisis_counts = merged_df.groupby('Type of Crisis')['title'].count()

# Plotting Total Movies by Crisis Type
plt.figure(figsize=(14, 7))
crisis_counts.plot(kind='bar', color='lightblue')
plt.title("Total Movies by Crisis Type")
plt.xlabel("Type of Crisis")
plt.ylabel("Number of Movies")
plt.xticks(rotation=90)
plt.tight_layout()  # To avoid cut-off labels
plt.show()

# Option 3: Movies by Year for a Specific Crisis Type (Example: Africa)
africa_movies = merged_df[merged_df['Type of Crisis'] == 'Africa']
africa_movies_by_year = africa_movies.groupby('release_year')['title'].count()

# Plotting Movies by Year for Africa Crisis
plt.figure(figsize=(10, 6))
africa_movies_by_year.plot(kind='line', marker='o')
plt.title("Movies by Year for Africa Crisis")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.grid(True)
plt.show()
