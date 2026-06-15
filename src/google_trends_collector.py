from pytrends.request import TrendReq
import pandas as pd
import os
import time

KEYWORDS = [
    "Labubu",
    "Miu Miu",
    "Loewe",
    "chocolate brown",
    "suede tote"
]

print("Starting Google Trends collection...")

try:
    time.sleep(3)

    pytrends = TrendReq(
        hl="en-US",
        tz=330
    )

    pytrends.build_payload(
        KEYWORDS,
        timeframe="today 3-m"
    )

    data = pytrends.interest_over_time()

    if data.empty:
        raise Exception("No data returned")

    data.to_csv(
        "data/google_trends.csv"
    )

    print("Fresh trend data saved!")

except Exception as e:

    print("\nGoogle Trends Error:")
    print(e)

    if os.path.exists(
        "data/google_trends.csv"
    ):

        print(
            "Using previously saved trend data."
        )

    else:

        print(
            "No backup trend data available."
        )

        backup = pd.DataFrame({
            "Labubu": [30],
            "Miu Miu": [50],
            "Loewe": [40],
            "chocolate brown": [25],
            "suede tote": [20]
        })

        backup.to_csv(
            "data/google_trends.csv",
            index=False
        )

        print(
            "Created emergency backup dataset."
        )
