import json

with open("data/trend_score.json", "r") as file:
    trend = json.load(file)

trend_name = trend["trend"].lower()

brand_map = {

    "old money": [
        "Ralph Lauren",
        "Loro Piana",
        "Brunello Cucinelli",
        "Hermès"
    ],

    "quiet luxury": [
        "The Row",
        "Loro Piana",
        "Hermès",
        "Khaite"
    ],

    "suede": [
        "Miu Miu",
        "Prada",
        "Loewe",
        "Coach"
    ],

    "labubu": [
        "Pop Mart"
    ]
}

brands = brand_map.get(
    trend_name,
    ["Unknown"]
)

result = {
    "trend": trend_name,
    "brands": brands
}

with open(
    "data/brand_intelligence.json",
    "w"
) as file:
    json.dump(result, file, indent=4)

print("\nAffected Brands")
print("=" * 40)

for brand in brands:
    print("-", brand)
