from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key
API_KEY = os.getenv("TMDB_API_KEY")
print(f"API Key: {API_KEY}")

