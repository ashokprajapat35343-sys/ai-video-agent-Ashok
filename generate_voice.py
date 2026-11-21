from gtts import gTTS
import json
import os

os.makedirs("audio", exist_ok=True)

data = json.load(open("scripts.json"))

for item in data:
    tts = gTTS(item["script"])
    tts.save(f"audio/{item['topic']}.mp3")
