import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

topics = json.load(open("trends.json"))

result = []

for topic in topics:

    prompt = f"""
Create a viral 60-second YouTube Shorts script.

Topic:
{topic}

Provide:
1. Hook
2. Main points
3. CTA
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    result.append({
        "topic": topic,
        "script": response.choices[0].message.content
    })

with open("scripts.json","w") as f:
    json.dump(result,f,indent=2)

print("Scripts generated")
