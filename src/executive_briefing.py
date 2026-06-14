import json

with open("data/trend_score.json", "r") as file:
    score = json.load(file)

with open("data/trend_explanation.txt", "r") as file:
    explanation = file.read()

briefing = f"""
AURA EXECUTIVE BRIEFING
==================================================

Top Trend:
{score['trend']}

Trend Score:
{score['score']}/100

Status:
{score['status']}

Market Insight:
{explanation}

Recommendation:
Monitor trend development and identify
luxury brands positioned to benefit.

==================================================
"""

with open(
    "data/executive_briefing.txt",
    "w"
) as file:
    file.write(briefing)

print(briefing)
