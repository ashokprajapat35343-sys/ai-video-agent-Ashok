from moviepy import ImageClip
import os

os.makedirs("output", exist_ok=True)

video = (
    ImageClip("background.jpg")
    .with_duration(10)
)

video.write_videofile(
    "output/test_short.mp4",
    fps=24
)

print("Video created successfully")
