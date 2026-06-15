import json

# Mock Reddit data for now
# Later we'll connect Reddit API

reddit_signals = [

    {
        "trend": "old money",
        "mentions": 124,
        "sentiment": "positive"
    },

    {
        "trend": "quiet luxury",
        "mentions": 89,
        "sentiment": "positive"
    },

    {
        "trend": "suede bags",
        "mentions": 42,
        "sentiment": "neutral"
    }

]

with open(
    "data/reddit_signals.json",
    "w"
) as file:

    json.dump(
        reddit_signals,
        file,
        indent=4
    )

print("Reddit signals saved!")
