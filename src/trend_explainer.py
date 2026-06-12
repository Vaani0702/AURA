import json
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

with open("data/discovered_trends.json", "r") as file:
    trends = json.load(file)

top_trend = trends[0]["trend"]

prompt = f"""
Explain why this trend may be growing:

Trend: {top_trend}

Give:
1. What it is
2. Why it matters
3. Luxury/fashion relevance
4. Confidence score out of 10
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

analysis = response.choices[0].message.content

print("\nAURA TREND EXPLANATION\n")
print(analysis)

with open("data/trend_explanation.txt", "w") as file:
    file.write(analysis)

print("\nExplanation saved!")
