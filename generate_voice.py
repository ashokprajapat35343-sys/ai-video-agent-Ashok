from gtts import gTTS
import json
import os

os.makedirs("audio", exist_ok=True)

data = json.load(open("scripts.json"))

for item in data:

    topic = item["topic"].replace(" ","_")

    tts = gTTS(item["script"])

    tts.save(
        f"audio/{topic}.mp3"
    )

print("Audio generated")
