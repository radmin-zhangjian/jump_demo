#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__auth__ = 'YU'

import os
import PIL, numpy
import matplotlib.pyplot as plt

def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png') #获取手机当前界面的实时截图
    os.system('adb pull /sdcard/screen.png') #下载当前截图到电脑当前文件夹下
    numpy.array(PIL.Image.open('screen.png')) #把打开的文件转换成多维数组

figure = plt.figure() #创建一个空白的图片对象
axes_image = plt.imshow(get_screen_image(), animated=True) #把获取的图片画在坐标轴上
plt.show()