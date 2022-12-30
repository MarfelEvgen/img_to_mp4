import glob
import os
import cv2
from PIL import Image

SOURCE_DIR = 'images/'
files = os.listdir(SOURCE_DIR)

img_video_width = 414
img_video_height = 842

for f in files:
    img = Image.open(f'images/{f}')
    width = img_video_width
    height = img_video_height

frameSize = (img_video_width, img_video_height)

suffix = '_banners'

out = cv2.VideoWriter(f'd:\_spizgeno_s_figmaweb{suffix}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 0.5, frameSize)

for filename in glob.glob('images/*'):
    img = cv2.imread(filename)
    out.write(img)

out.release()


