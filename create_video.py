import os
from moviepy import ColorClip, AudioFileClip

audio_files = [
    f for f in os.listdir("audio")
    if f.endswith(".mp3")
]

audio = AudioFileClip(
    f"audio/{audio_files[0]}"
)

video = ColorClip(
    size=(1080,1920),
    color=(15,15,15),
    duration=audio.duration
)

video = video.with_audio(audio)

video.write_videofile(
    "output/test_short.mp4",
    fps=24
)
