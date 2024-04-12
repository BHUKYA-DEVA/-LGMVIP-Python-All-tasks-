from moviepy.editor import *

video_clip=VideoFileClip("python/video1.mp4")

sec_5_clip=video_clip.subclip(0,5)
sec_5_clip.write_gif("first.gif")