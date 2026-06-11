import pandas as pd
import json

# Load CSV
df = pd.read_csv("../data/google_trends.csv")

# Remove incomplete Google Trends rows
df = df[df["isPartial"] == False]

trend_columns = [
    "quiet luxury",
    "old money",
    "suede",
    "minimalism"
]

results = []

for trend in trend_columns:

    # Average of latest 7 days
    last_7_days = df[trend].tail(7).mean()

    # Average of previous 7 days
    previous_7_days = df[trend].tail(14).head(7).mean()

    change = round(last_7_days - previous_7_days, 2)

    if change > 1:
        status = "Rising"
    elif change < -1:
        status = "Falling"
    else:
        status = "Stable"

    results.append({
        "trend": trend,
        "current": float(round(last_7_days, 2)),
        "previous": float(round(previous_7_days, 2)),
        "change": float(change),
        "status": status
    })

print("\nDEBUG\n")

for item in results:
    print(item)

# Sort by strongest growth
results.sort(
    key=lambda x: x["change"],
    reverse=True
)

# Find only rising trends
rising_trends = [
    item
    for item in results
    if item["change"] > 0
]

# Choose top trend
if rising_trends:
    top_trend = rising_trends[0]
else:
    top_trend = {
        "trend": "No Significant Trend",
        "current": 0,
        "previous": 0,
        "change": 0,
        "status": "No Rising Trend Found"
    }

# Save JSON report
with open("../data/trend_report.json", "w") as file:
    json.dump(top_trend, file, indent=4)

print("\nAURA Trend Report Saved!")
print(top_trend)