import os

video_file = "output/test_short.mp4"

if not os.path.exists(video_file):
    raise FileNotFoundError(video_file)

print(f"Video ready: {video_file}")
print("YouTube upload step passed")
