import os
from PIL import Image
import glob

picdir = r'c:\\showmecode\\code\\6'
file = glob.glob(os.path.join(picdir, '*.jpg'))
if not os.path.exists('thumDir'):
    os.mkdir('thumDir')

width = 640
height = 1136
rate = height / width

for img in file:
    p, f = os.path.split(img)
    img = Image.open(img)
    imgSize = img.size
    Max = max(imgSize)
    Min = min(imgSize)
    imgRate = Max / Min
    if Max >= height and Min >= width:
        n = Min / width
        m = Max / height
        if n > m:
            img = img.resize((Max / (n + 1), Min / (n + 1)))
        else:
            img = img.resize((Max / (m + 1), Min / (m + 1)))
    elif Max > height and Min < width:
        m = Max / height
        img = img.resize((Max / m, Min / m))
    elif Max < height and Min > width:
        n = Min / width
        img = img.resize((Max / n), Min / n)
    else:
        img = img.resize((Max, Min))

    img.save(os.path.join('thumDir', f))
