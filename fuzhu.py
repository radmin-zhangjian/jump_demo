#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__auther__ = 'YU'

import os
import PIL, numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

need_update = True

def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png') #获取手机当前界面的实时截图
    os.system('adb pull /sdcard/screen.png') #下载当前截图到电脑当前文件夹下
    return numpy.array(PIL.Image.open('screen.png')) #把打开的文件转换成多维数组

# 计算玄的长度
def jump_to_next(point1, point2):
    x1, y1 = point1; x2, y2 = point2
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance*1.35)))
    
# 绑定的鼠标单击事件
def on_click(event, coor=[]):
    global need_update
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())
    need_update = True
    
# 重画图像
def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image()) #更新图片
        need_update = False
    return axes_image,

figure = plt.figure() #创建一个空白的图片对象
axes_image = plt.imshow(get_screen_image(), animated=True) #把获取的图片画在坐标轴上
figure.canvas.mpl_connect('button_press_event', on_click)
ani = FuncAnimation(figure, update_screen, interval=50, blit=True)
plt.show()
