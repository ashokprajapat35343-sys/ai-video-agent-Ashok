import os
import json
import requests

topic = json.load(open("trends.json"))[0]

headers = {
    "Authorization": os.environ["PEXELS_API_KEY"]
}

url = f"https://api.pexels.com/videos/search?query={topic}&per_page=1"

response = requests.get(url, headers=headers)

data = response.json()

video_url = data["videos"][0]["video_files"][0]["link"]

video_data = requests.get(video_url)

os.makedirs("clips", exist_ok=True)

with open("clips/trending.mp4", "wb") as f:
    f.write(video_data.content)

print("Video downloaded")
