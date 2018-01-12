# -*-coding:utf-8-*-
import os
from PIL import Image




filename = 'autojump.png'
filename1 = 'test.png'


def cuti():
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print('..')
    if os.path.exists(filename1):
        os.remove(filename1)
    else:
        print('..')
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png .')

    img = Image.open('C:\\Users\chufusheng\Desktop\\test1.png')
    region = (100, 100, 500, 800)
    # 裁切图片
    cropImg = img.crop(region)

    # 保存裁切后的图片
    cropImg.save('test.png')




cuti()