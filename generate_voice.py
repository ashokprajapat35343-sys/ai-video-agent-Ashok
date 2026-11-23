from gtts import gTTS
import json
import os

os.makedirs("audio", exist_ok=True)

with open("scripts.json", "r") as f:
    data = json.load(f)

print("Scripts loaded:", len(data))

for item in data:

    topic = item["topic"].replace(" ", "_")

    filename = f"audio/{topic}.mp3"

    print("Creating:", filename)

    tts = gTTS(text=item["script"], lang="en")

    tts.save(filename)

print("Audio generated successfully")
print("Files:", os.listdir("audio"))
