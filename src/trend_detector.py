import pandas as pd
import json

# Load CSV
df = pd.read_csv("../data/google_trends.csv")

# Remove incomplete rows
df = df[df["isPartial"] == False]

# Last 2 complete days
today = df.iloc[-1]
yesterday = df.iloc[-2]

trend_columns = [
    "quiet luxury",
    "old money",
    "suede",
    "minimalism"
]

results = []

for trend in trend_columns:

    current = today[trend]
    previous = yesterday[trend]

    change = current - previous

    if change > 0:
        status = "Rising"
    elif change < 0:
        status = "Falling"
    else:
        status = "Stable"

    results.append({
        "trend": trend,
        "current": int(current),
        "previous": int(previous),
        "change": int(change),
        "status": status
    })

# Sort by biggest increase
results.sort(key=lambda x: x["change"], reverse=True)

top_trend = results[0]

# Save JSON report
with open("../data/trend_report.json", "w") as file:
    json.dump(top_trend, file, indent=4)

print("AURA Trend Report Saved!")
print(top_trend)