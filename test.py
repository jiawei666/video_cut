from moviepy import VideoFileClip, ImageSequenceClip, TextClip, CompositeVideoClip, ImageClip, vfx,concatenate_videoclips




# 图片文件列表和每张图片的显示时长
image_files = ["转场图片.jpg", "转场图片2.jpg", "转场图片.jpg", "转场图片2.jpg", "转场图片.jpg"]
image_duration = 5  # 每张图片的持续时间，单位：秒

# 计算图片的总时长
total_image_duration = len(image_files) * image_duration

# 背景视频
background = VideoFileClip("特朗普.mp4")
# 如果背景视频的时长小于图片的总时长，循环背景视频直到时长足够
if background.duration < total_image_duration:

    background = background.with_effects([vfx.Loop(duration=total_image_duration)])

# 创建每张图片的 ImageClip
image_clips = []
for i, image_file in enumerate(image_files):
    start = 1
    if len(image_clips) > 0:
        start = image_clips[i-1].end

    # top = background.h * 0.25
    # left = background.w / 2


    image = ImageClip(image_file).resized(width=500).with_start(start).with_duration(4)
    print('->>>>>>',background.h, background.w)
    print('->>>>>>',image.h, image.w)
    # top = (background.h - image.h) / 2
    image = image.with_position(("center", 0.25), relative=True)

        # .with_start(t=start).with_end(t=end)
    image = image.with_effects([vfx.CrossFadeIn(duration=1)])
    image = image.with_effects([vfx.SlideOut(duration=1, side='right')])

    image_clips.append(image)




# 将背景视频和图片合成
final_video = CompositeVideoClip([background] + image_clips)

# 输出最终的视频
final_video.write_videofile("result2.mp4")