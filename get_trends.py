from pytrends.request import TrendReq
import json

pytrends = TrendReq(hl='en-US', tz=360)

keywords = [
    "AI",
    "ChatGPT",
    "Tesla",
    "Bitcoin",
    "YouTube",
    "Technology"
]

with open("trends.json", "w") as f:
    json.dump(keywords[:2], f)

print("Saved trending topics")
