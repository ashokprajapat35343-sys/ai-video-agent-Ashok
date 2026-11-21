import os

video_file = "output/test_short.mp4"

if os.path.exists(video_file):
    print(f"Found video: {video_file}")
else:
    raise FileNotFoundError(video_file)

print("Ready for YouTube upload")
