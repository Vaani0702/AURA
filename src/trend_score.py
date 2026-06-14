import json

# Load latest trend report
with open("data/trend_report.json", "r") as file:
    trend = json.load(file)

change = float(trend.get("change", 0))

# -------------------------
# Growth Score
# -------------------------

if change > 20:
    growth_score = 40
elif change > 10:
    growth_score = 30
elif change > 0:
    growth_score = 20
else:
    growth_score = 10

# -------------------------
# Momentum Score
# -------------------------

if change > 15:
    momentum_score = 30
elif change > 5:
    momentum_score = 20
else:
    momentum_score = 10

# -------------------------
# Confidence Score
# -------------------------

confidence_score = 20

# -------------------------
# Discovery Score
# -------------------------

confidence_score += 10

# -------------------------
# Final Score
# -------------------------

trend_score = (
    growth_score
    + momentum_score
    + confidence_score
)

result = {
    "trend": trend["trend"],
    "score": trend_score,
    "status": trend["status"],
    "change": trend["change"]
}

with open("data/trend_score.json", "w") as file:
    json.dump(result, file, indent=4)

print("\nAURA Trend Score")
print("=" * 40)
print(f"Trend: {trend['trend']}")
print(f"Score: {trend_score}/100")
print(f"Status: {trend['status']}")
