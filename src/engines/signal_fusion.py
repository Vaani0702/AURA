import json

with open(
    "data/reddit_signals.json"
) as file:

    reddit = json.load(file)

with open(
    "data/discovered_trends.json"
) as file:

    trends = json.load(file)

combined = []

for trend in trends:

    trend_name = trend["trend"].lower()

    reddit_match = next(
        (
            r for r in reddit
            if r["trend"].lower() == trend_name
        ),
        None
    )

    combined.append({

        "trend": trend["trend"],

        "google_score":
            trend["score"],

        "reddit_mentions":
            reddit_match["mentions"]
            if reddit_match else 0,

        "sentiment":
            reddit_match["sentiment"]
            if reddit_match else "unknown"
    })

with open(
    "data/intelligence_report.json",
    "w"
) as file:

    json.dump(
        combined,
        file,
        indent=4
    )

print("Intelligence report created!")
