import os
from moviepy import ColorClip, AudioFileClip

os.makedirs("output", exist_ok=True)

audio_files = [
    f for f in os.listdir("audio")
    if f.endswith(".mp3")
]

if len(audio_files) == 0:
    raise Exception(
        f"No mp3 files found in audio folder. Files: {os.listdir('audio')}"
    )

audio_file = audio_files[0]

audio = AudioFileClip(
    f"audio/{audio_file}"
)

video = ColorClip(
    size=(1080, 1920),
    color=(15, 15, 15),
    duration=audio.duration
)

video = video.with_audio(audio)

video.write_videofile(
    "output/test_short.mp4",
    fps=24
)

print("Video created")
