import pandas as pd  # Ensure pandas is imported

# Load the Excel file
df = pd.read_excel("political_events.xlsx")

# Save as CSV
df.to_csv("political_events.csv", index=False)

print("Excel file converted to CSV successfully!")

