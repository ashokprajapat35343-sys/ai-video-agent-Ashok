from moviepy import ColorClip, AudioFileClip

audio = AudioFileClip(
    "audio/Artificial_Intelligence.mp3"
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

print("Video generated")
