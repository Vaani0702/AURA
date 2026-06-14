import json

with open("data/trend_score.json", "r") as file:
    trend = json.load(file)

name = trend["trend"]

explanations = {
    "old money":
        """
Old Money reflects growing consumer interest in timeless luxury,
heritage fashion, premium materials, and understated wealth.

Brands likely benefiting:
- Ralph Lauren
- Brunello Cucinelli
- Loro Piana

Consumer drivers:
- Quiet luxury movement
- Anti-fast-fashion sentiment
- Long-term value purchasing
""",

    "quiet luxury":
        """
Quiet Luxury emphasizes craftsmanship,
minimal branding, and premium quality.

Brands likely benefiting:
- The Row
- Loro Piana
- Hermès
"""
}

report = explanations.get(
    name.lower(),
    "No explanation available."
)

with open(
    "data/trend_explanation.txt",
    "w"
) as file:
    file.write(report)

print(report)
