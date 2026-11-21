from openai import OpenAI
import json

client = OpenAI()

topics = json.load(open("trends.json"))

results = []

for topic in topics:
    prompt = f"""
    Create a viral YouTube Shorts script about:
    {topic}

    Format:
    Hook
    Main Content
    CTA

    Length: 60 seconds.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    results.append({
        "topic": topic,
        "script": response.choices[0].message.content
    })

json.dump(results, open("scripts.json", "w"), indent=2)
