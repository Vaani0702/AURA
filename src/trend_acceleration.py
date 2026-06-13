import json

with open("data/trend_history.json", "r") as file:
    history = json.load(file)

if len(history) < 2:
    print("Not enough data for acceleration analysis.")
    exit()

latest = history[-1]
previous = history[-2]

acceleration = latest["current"] - previous["current"]

print("\nTREND ACCELERATION")
print("=" * 40)
print("Trend:", latest["trend"])
print("Acceleration:", round(acceleration, 2))

if acceleration > 2:
    print("Status: BREAKOUT TREND")

elif acceleration > 0:
    print("Status: GROWING")

else:
    print("Status: STABLE / DECLINING")
