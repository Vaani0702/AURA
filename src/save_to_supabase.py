import os
import json

from dotenv import load_dotenv
from supabase import create_client



load_dotenv()



url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

with open("../data/trend_report.json", "r") as file:
    trend = json.load(file)

data = {
    "trend": trend["trend"],
    "current_score": trend["current"],
    "previous_score": trend["previous"],
    "change": trend["change"],
    "status": trend["status"]
}

response = supabase.table("trend_reports").insert(data).execute()

print("Saved to Supabase!")
print(response)
