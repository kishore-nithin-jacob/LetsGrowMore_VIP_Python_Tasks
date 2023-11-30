# TASK - 1
# GIF CREATOR

import os
import urllib.request
from moviepy.editor import VideoFileClip
from IPython.display import display, Image

def download_video(video_url, output_path='input_video.mp4'):
    urllib.request.urlretrieve(video_url, output_path)

def convert_video_to_gif(video_path, gif_path='output.gif', start_time=0, end_time=None):
    clip = VideoFileClip(video_path).subclip(start_time, end_time)
    clip.write_gif(gif_path, fps=10)

video_url = '<Video URL>'

# Download video
download_video(video_url)

# Convert video to gif
convert_video_to_gif('input_video.mp4')

# Display the GIF
display(Image(filename='output.gif'))
