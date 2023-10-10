'''
Author: wolffy
Date: 2023-10-10 17:37:20
LastEditors: fengtao92 1440913385@qq.com
LastEditTime: 2023-10-10 17:40:32
FilePath: /metahuman/Audio/microphone.py
Description: 项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Copyright (c) 2023 by 北京光线传媒股份有限公司, All Rights Reserved. 
'''
import pyaudio
import numpy as np

# 打开麦克风
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
# 控制麦克风
while True:
    data = stream.read(1024)
    audio = np.frombuffer(data, dtype=np.int16)
    volume = np.max(audio)
    if volume >5000:
        print("声音太大了！")
    else:
        print("声音正常")
# 关闭麦克风
# stream.stop_stream()
# stream.close()
# p.terminate()