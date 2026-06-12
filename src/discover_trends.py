import json

discovered_trends = []

sample_trends = [
    "Labubu",
    "Quiet Luxury",
    "Suede Bags",
    "Old Money Aesthetic",
    "Mob Wife Aesthetic"
]

for trend in sample_trends:

    score = len(trend) * 5

    discovered_trends.append({
        "trend": trend,
        "source": "discovery_engine",
        "score": score
    })

discovered_trends.sort(
    key=lambda x: x["score"],
    reverse=True
)

with open("data/discovered_trends.json", "w") as file:
    json.dump(
        discovered_trends,
        file,
        indent=4
    )

print("\nTOP DISCOVERED TRENDS\n")

for trend in discovered_trends:
    print(trend)

print("\nDiscovery Complete!")
