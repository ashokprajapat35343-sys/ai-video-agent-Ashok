import json

topics = ["AI News", "Latest Tech"]

scripts = []

for topic in topics:
    scripts.append({
        "topic": topic,
        "script": f"""
Hook:
Did you know this about {topic}?

Main:
Here are the biggest updates today.

CTA:
Follow for more tech news.
"""
    })

with open("scripts.json", "w") as f:
    json.dump(scripts, f, indent=2)

print("Scripts generated")
