import pandas as pd
import json
import os

if not os.path.exists(
    "data/google_trends.csv"
):
    print("No trend data found.")
    exit()

df = pd.read_csv(
    "data/google_trends.csv"
)

trend_scores = {}

for column in df.columns:

    if column.lower() == "date":
        continue

    try:

        values = df[column].dropna()

        if len(values) < 2:
            continue

        current = values.iloc[-1]
        previous = values.iloc[-2]

        change = current - previous

        trend_scores[column] = {
            "current": float(current),
            "previous": float(previous),
            "change": float(change)
        }

    except:
        pass

if not trend_scores:

    result = {
        "trend": "No Significant Trend",
        "current": 0,
        "previous": 0,
        "change": 0,
        "status": "No Rising Trend Found"
    }

else:

    top_trend = max(
        trend_scores,
        key=lambda x:
        trend_scores[x]["change"]
    )

    data = trend_scores[top_trend]

    result = {
        "trend": top_trend,
        "current": round(
            data["current"], 2
        ),
        "previous": round(
            data["previous"], 2
        ),
        "change": round(
            data["change"], 2
        ),
        "status": (
            "Growing"
            if data["change"] > 0
            else "Falling"
        )
    }

with open(
    "data/trend_report.json",
    "w"
) as file:

    json.dump(
        result,
        file,
        indent=4
    )

print("\nTrend Detection Complete")
print("=" * 40)
print(result)
