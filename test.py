from moviepy import VideoFileClip, TextClip, CompositeVideoClip, ImageClip, vfx

# 背景视频
background = (
    VideoFileClip("特朗普.mp4")
    .subclipped(0, 10)
    .with_volume_scaled(0.8)
)


# 图片文件列表和每张图片的显示时长
image_files = ["转场图片.jpg", "转场图片.jpg", "转场图片.jpg", "转场图片.jpg", "转场图片.jpg"]
image_duration = 5  # 每张图片的持续时间，单位：秒

# 计算图片的总时长
total_image_duration = len(image_files) * image_duration

# 如果背景视频的时长小于图片的总时长，循环背景视频直到时长足够
if background.duration < total_image_duration:
    
    background = background.with_effects([vfx.Loop(duration=total_image_duration)])

# 创建每张图片的 ImageClip
image_clips = []
for i, image_file in enumerate(image_files):
    image = ImageClip(image_file).resized(height=background.h / 3).with_position('center').with_duration(image_duration) 

    # 如果是第一个图片，则不需要转场效果
    if i > 0:
        image = image.with_effects([vfx.CrossFadeIn(duration=1)])

    image_clips.append(image)

# txt_clip = TextClip(
#     font="微软雅黑.ttf",
#     text="测试测试测试测试",
#     font_size=70,
#     color='white'
# ).with_duration(total_image_duration).with_position('center')


# 将背景视频和图片合成
final_video = CompositeVideoClip([background] + image_clips)

# 输出最终的视频
final_video.write_videofile("result2.mp4", fps=24)