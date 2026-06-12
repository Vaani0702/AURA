import json
from pytrends.request import TrendReq

# Connect to Google Trends
pytrends = TrendReq(timeout=(10, 25))

# Seed trends
keywords = [
    "quiet luxury",
    "old money",
    "suede"
]

# Store discovered trends
discovered_trends = []

for keyword in keywords:

    try:

        pytrends.build_payload(
            [keyword],
            timeframe="today 3-m"
        )

        related = pytrends.related_queries()

        print("\n" + "=" * 50)
        print("SEED TREND:", keyword)
        print("=" * 50)

        if keyword in related:

            rising = related[keyword]["rising"]

            if rising is not None:

                print(rising.head(10))

                for _, row in rising.head(5).iterrows():

                    discovered_trends.append({
                        "trend": str(row["query"]),
                        "source": keyword,
                        "score": int(row["value"])
                    })

            else:

                print("No rising trends found.")

    except Exception as e:

        print(f"\nError for {keyword}")
        print(e)

# Sort by score
discovered_trends.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Save results
with open("data/discovered_trends.json", "w") as file:

    json.dump(
        discovered_trends,
        file,
        indent=4
    )

print("\n" + "=" * 50)
print("DISCOVERED TRENDS")
print("=" * 50)

for trend in discovered_trends[:10]:
    print(trend)

print("\nSaved discovered trends!")
