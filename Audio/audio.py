'''
Author: wolffy
Date: 2023-10-10 16:58:37
LastEditors: fengtao92 1440913385@qq.com
LastEditTime: 2023-10-10 18:15:38
FilePath: /metahuman/Audio/audio.py
Description: 项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Copyright (c) 2023 by 北京光线传媒股份有限公司, All Rights Reserved. 
'''
import pygame
import sounddevice as sd

devs = sd.query_devices()
print('声卡')
for dev in devs:
    print(dev['name'])

pygame.mixer.init(devicename='Zoom Audio (1ch)')

pygame.mixer.music.load(filename='/Users/admin/Desktop/1.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(2)
while pygame.mixer.music.get_busy():
    pass
