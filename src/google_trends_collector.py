from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=330)

keywords = [
    "quiet luxury",
    "old money",
    "suede",
    "minimalism"
]

pytrends.build_payload(
    keywords,
    timeframe='today 3-m'
)

data = pytrends.interest_over_time()

data.to_csv("../data/google_trends.csv")
print("Saved successfully")