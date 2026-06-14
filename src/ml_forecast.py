import json
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

with open("data/trend_history.json", "r") as file:
    history = json.load(file)

if len(history) < 5:
    print("Need at least 5 records.")
    exit()

df = pd.DataFrame(history)

X = np.arange(len(df)).reshape(-1, 1)
y = df["current"]

model = LinearRegression()
model.fit(X, y)

next_day = np.array([[len(df)]])
prediction = model.predict(next_day)

print("\nML FORECAST")
print("=" * 40)
print("Next predicted score:", round(float(prediction[0]), 2))
