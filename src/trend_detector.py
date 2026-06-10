import pandas as pd

# Load the CSV
df = pd.read_csv("../data/google_trends.csv")

# Remove incomplete Google Trends rows
df = df[df["isPartial"] == False]

# Get the last two complete days
today = df.iloc[-1]
yesterday = df.iloc[-2]

print("\nAURA TREND REPORT")
print("=" * 40)

# Trend columns only
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
        status = "Rising 📈"
    elif change < 0:
        status = "Falling 📉"
    else:
        status = "Stable ➖"

    results.append({
        "trend": trend,
        "current": current,
        "previous": previous,
        "change": change,
        "status": status
    })

# Sort by biggest increase
results.sort(key=lambda x: x["change"], reverse=True)

for item in results:
    print(f"""
Trend: {item['trend']}
Current Score: {item['current']}
Previous Score: {item['previous']}
Change: {item['change']}
Status: {item['status']}
""")