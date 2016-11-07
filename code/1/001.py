#_*_coding:utf-8_*_
'''图片处理'''
import Image
import ImageDraw
import ImageFont
import os


def drawNumber(jpg):
    infile = os.path.splitext(jpg)
    if infile[1] == '.jpg':
        im = Image.open(jpg)
        x, y = im.size
        ImageDrawer = ImageDraw.Draw(im)
        ttfont = ImageFont.truetype("arial.ttf", 100)
        ImageDrawer.text((x - 300, y - 600),"99",
                         font=ttfont, fill=(255, 0, 0))
        im.save('n1.jpg', "JPEG")
    else:
        print "Please input jpg file!"
