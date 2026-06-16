import json
import os


DATA_DIR = "data"

GOOGLE_FILE = os.path.join(
    DATA_DIR,
    "trend_report.json"
)

REDDIT_FILE = os.path.join(
    DATA_DIR,
    "reddit_signals.json"
)

OUTPUT_FILE = os.path.join(
    DATA_DIR,
    "intelligence_report.json"
)


google_data = {}

reddit_data = []


if os.path.exists(GOOGLE_FILE):

    with open(GOOGLE_FILE, "r") as f:
        google_data = json.load(f)


if os.path.exists(REDDIT_FILE):

    with open(REDDIT_FILE, "r") as f:
        reddit_data = json.load(f)


trend = google_data.get(
    "trend",
    "Unknown"
)

change = google_data.get(
    "change",
    0
)

status = google_data.get(
    "status",
    "Unknown"
)

reddit_mentions = 0
sentiment = "Unknown"


for item in reddit_data:

    if item["trend"].lower() == trend.lower():

        reddit_mentions = item["mentions"]
        sentiment = item["sentiment"]


score = max(
    0,
    min(
        100,
        50
        + change * 10
        + reddit_mentions * 0.2
    )
)


report = {

    "trend": trend,

    "change": change,

    "status": status,

    "reddit_mentions": reddit_mentions,

    "sentiment": sentiment,

    "intelligence_score": round(score, 2)

}


with open(
    OUTPUT_FILE,
    "w"
) as f:

    json.dump(
        report,
        f,
        indent=4
    )


print()

print("=" * 50)

print("AURA Intelligence Report")

print("=" * 50)

print(json.dumps(report, indent=4))
