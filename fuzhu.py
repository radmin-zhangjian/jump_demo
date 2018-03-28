#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__auth__ = 'YU'

import os

def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')
    
get_screen_image()