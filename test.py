from moviepy import VideoFileClip, TextClip, CompositeVideoClip, ImageClip

# Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# Reduce the audio volume to 80% of its original volume

clip = (
    VideoFileClip("特朗普.mp4")
    .subclipped(5, 8)
    .with_volume_scaled(0.8)
)

image_clip = ImageClip("上海市·上海_2024年05月.png").resized(width=200).with_position('center').with_duration(3)  # For a picture

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip(
    font="微软雅黑.ttf",
    text="Hello there!",
    font_size=70,
    color='white'
).with_duration(3).with_position('center')



# Overlay the text clip on the first video clip
final_video = CompositeVideoClip([clip, image_clip, txt_clip])
final_video.write_videofile("result2.mp4")