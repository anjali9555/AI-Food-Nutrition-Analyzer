import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Fetch and print all available models for your specific API key
print("Available Models for your API Key:")
for model in client.models.list().data:
    print(f"- {model.id}")