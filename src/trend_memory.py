import json
from datetime import datetime

# Load latest trend report

with open("data/trend_report.json", "r") as file:
    trend = json.load(file)

# Load history

try:
    with open("data/trend_history.json", "r") as file:
        history = json.load(file)

except:
    history = []

# Create memory entry

entry = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "trend": trend["trend"],
    "current": trend["current"],
    "change": trend["change"],
    "status": trend["status"]
}

history.append(entry)

# Save history

with open("data/trend_history.json", "w") as file:
    json.dump(history, file, indent=4)

print("Trend memory updated!")
print(entry)
