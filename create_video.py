from moviepy import VideoFileClip, AudioFileClip

video = VideoFileClip("clips/trending.mp4")

audio = AudioFileClip("audio/Artificial_Intelligence.mp3")

video = video.with_audio(audio)

video.write_videofile(
    "output/test_short.mp4",
    fps=24
)
