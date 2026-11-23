import os
from moviepy import ColorClip, AudioFileClip

os.makedirs("output", exist_ok=True)

audio_files = [
    f for f in os.listdir("audio")
    if f.endswith(".mp3")
]

if not audio_files:
    raise Exception("No audio files found")

audio = AudioFileClip(
    f"audio/{audio_files[0]}"
)

video = ColorClip(
    size=(1080, 1920),
    color=(20, 20, 20),
    duration=audio.duration
)

video = video.with_audio(audio)

video.write_videofile(
    "output/test_short.mp4",
    fps=24
)
