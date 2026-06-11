import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Read trend report JSON
with open("../data/trend_report.json", "r") as file:
    trend_data = json.load(file)

# Build prompt
prompt = f"""
You are AURA's luxury trend analyst.

Analyze this trend:

Trend: {trend_data['trend']}
Current Score: {trend_data['current']}
Previous Score: {trend_data['previous']}
Change: {trend_data['change']}
Status: {trend_data['status']}

Give:
1. Short summary
2. Why it matters
3. Confidence level

Keep the response under 100 words.
"""

# Send to Groq
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
with open("../data/analysis_report.txt", "w") as file:
    file.write(analysis)

with open("../data/analysis_report.json", "w") as file:
    json.dump({"analysis": analysis}, file)
print("\nAURA ANALYSIS")
print("=" * 50)
print(analysis)



print("\nAnalysis saved successfully!")