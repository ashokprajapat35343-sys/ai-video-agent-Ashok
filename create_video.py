from moviepy import ColorClip
import os

os.makedirs("output", exist_ok=True)

video = ColorClip(
    size=(1080, 1920),
    color=(0, 0, 255),
    duration=10
)

video.write_videofile(
    "output/test_short.mp4",
    fps=24
)

print("Video created")
