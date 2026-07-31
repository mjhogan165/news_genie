from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Read the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Ensure the API key is present
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY was not found. Add it to the project's .env file.")
