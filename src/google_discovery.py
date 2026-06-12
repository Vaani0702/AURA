from pytrends.request import TrendReq

pytrends = TrendReq()

keywords = [
    "quiet luxury",
    "old money",
    "suede"
]

for keyword in keywords:

    try:

        pytrends.build_payload(
            [keyword],
            timeframe="today 3-m"
        )

        related = pytrends.related_queries()

        print(f"\n{keyword.upper()}\n")

        if keyword in related:

            rising = related[keyword]["rising"]

            if rising is not None:
                print(rising.head())

    except Exception as e:

        print(f"Error for {keyword}")
        print(e)
