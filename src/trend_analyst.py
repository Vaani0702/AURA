import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Test trend
trend = "Suede"
current_score = 26
previous_score = 25

prompt = f"""
You are a luxury trend analyst.

Trend: {trend}
Current Score: {current_score}
Previous Score: {previous_score}

Explain what this trend means in 2-3 sentences.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)