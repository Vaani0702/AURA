import json
from datetime import datetime

with open("data/trend_report.json", "r") as file:
    trend = json.load(file)

try:
    with open("data/trend_history.json", "r") as file:
        history = json.load(file)
except:
    history = []

history.append({
    "date": datetime.now().strftime("%Y-%m-%d"),
    "trend": trend["trend"],
    "current": trend["current"],
    "previous": trend["previous"],
    "change": trend["change"],
    "status": trend["status"]
})

with open("data/trend_history.json", "w") as file:
    json.dump(history, file, indent=4)

print("History updated.")
