from moviepy.video.VideoClip import ColorClip
import os

os.makedirs("output", exist_ok=True)

video = ColorClip(
    size=(1080, 1920),
    color=(50, 50, 50),
    duration=10
)

video.write_videofile(
    "output/test_short.mp4",
    fps=24
)

print("Video created successfully")
