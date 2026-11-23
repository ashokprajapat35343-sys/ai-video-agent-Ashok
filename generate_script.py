import json

topics = json.load(open("trends.json"))

scripts = []

for topic in topics:
    scripts.append({
        "topic": topic,
        "script": f"""
Hook:
Breaking news about {topic}!

Main Content:
Here are the latest updates regarding {topic}.
This topic is currently trending and getting attention online.

Call To Action:
Follow for more trending news and updates.
"""
    })

with open("scripts.json", "w") as f:
    json.dump(scripts, f, indent=2)

print("Scripts generated successfully")
