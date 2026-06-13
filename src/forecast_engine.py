import json

with open("data/trend_history.json", "r") as file:
    history = json.load(file)

if len(history) < 3:
    print("Need at least 3 records for forecasting.")
    exit()

latest = history[-1]["current"]
previous = history[-2]["current"]
older = history[-3]["current"]

growth1 = latest - previous
growth2 = previous - older

average_growth = (growth1 + growth2) / 2

forecast = latest + average_growth

print("\nFORECAST")
print("=" * 40)
print("Current:", latest)
print("Predicted Next:", round(forecast, 2))
print("Average Growth:", round(average_growth, 2))
