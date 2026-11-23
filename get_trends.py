import json

topics = [
    "Artificial Intelligence",
    "ChatGPT",
    "Technology News",
    "Bitcoin"
]

with open("trends.json", "w") as f:
    json.dump(topics[:2], f)

print("Saved trending topics")
