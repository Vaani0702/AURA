import os
import json
import wandb

from dotenv import load_dotenv
from supabase import create_client



load_dotenv()



url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)
wandb.init(project="AURA")

with open("../data/trend_report.json", "r") as file:
    trend = json.load(file)

with open("../data/analysis_report.json", "r") as file:
    analysis_data = json.load(file)    

data = {
    "trend": trend["trend"],
    "current_score": trend["current"],
    "previous_score": trend["previous"],
    "change": trend["change"],
    "status": trend["status"],
    "analysis": analysis_data["analysis"]
}

response = supabase.table("trend_reports").insert(data).execute()

wandb.log({
    "trend": trend["trend"],
    "change": trend["change"],
    "status": trend["status"]
})

print("Saved to Supabase!")
print(response)
wandb.finish()
