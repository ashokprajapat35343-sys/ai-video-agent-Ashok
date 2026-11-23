import json
import os
import google.generativeai as genai

genai.configure(
    api_key=os.environ["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

topics = json.load(open("trends.json"))

scripts = []

for topic in topics:

    prompt = f"""
Create a viral YouTube Shorts script.

Topic: {topic}

Length: 45-60 seconds.

Include:
1. Hook
2. Key points
3. Call to action
"""

    response = model.generate_content(prompt)

    scripts.append({
        "topic": topic,
        "script": response.text
    })

with open("scripts.json", "w") as f:
    json.dump(scripts, f, indent=2)

print("Scripts generated")
