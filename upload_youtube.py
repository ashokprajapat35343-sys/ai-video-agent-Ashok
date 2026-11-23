import os

video = "output/test_short.mp4"

if not os.path.exists(video):
    raise FileNotFoundError(video)

print("Video exists")
print("Ready for upload")
