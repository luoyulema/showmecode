#赊购厂生成随机验证码
from PIL import ImageFont, ImageDraw, ImageFilter, Image
import random

randomColor = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
randomString = [random.randint(97, 122), random.randint(
    97, 122), random.randint(48, 57), random.randint(65, 90)]
height = 60
width = 240


def newPic(string):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    imgdraw = ImageDraw.Draw(img)
    ttfont = ImageFont.truetype('11111.ttf', 50)
    for x in range(width):
        for y in range(height):
            imgdraw.point((x, y), (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)))
    imgdraw.text((30, 10), string, font=ttfont, fill=randomColor)
    img = img.filter(ImageFilter.BLUR)
    img.save('1.jpg', 'jpeg')


def newString():
    str = randomString
    random.shuffle(str)
    s = ''
    for i in str:
        s += chr(i)
    return s
