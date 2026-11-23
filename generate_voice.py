from gtts import gTTS
import json
import os

if not os.path.exists("scripts.json"):
    raise FileNotFoundError(
        "scripts.json was not created"
    )

with open("scripts.json", "r") as f:
    data = json.load(f)

os.makedirs("audio", exist_ok=True)

for item in data:

    filename = (
        item["topic"]
        .replace(" ", "_")
        .replace("/", "_")
    )

    tts = gTTS(item["script"])
