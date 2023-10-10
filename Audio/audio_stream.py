'''
Author: wolffy
Date: 2023-10-10 17:16:02
LastEditors: fengtao92 1440913385@qq.com
LastEditTime: 2023-10-10 17:26:19
FilePath: /metahuman/Audio/audio_stream.py
Description: 项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Copyright (c) 2023 by 北京光线传媒股份有限公司, All Rights Reserved. 
'''
import pyaudio # pyaudio用conda安装
import sounddevice as sd
from pydub import AudioSegment

# 创建一个PyAudio音频输出流
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
# 将音频数据写入sounddevice虚拟声卡
mp3_file = AudioSegment.from_file('/Users/admin/Desktop/1.mp3')
audio_data = mp3_file.get_array_of_samples() # 获取音频数据
sd.play(audio_data)
while True:
    pass
# 关闭音频输出流
# stream.close()
# p.terminate()

# # 创建一个PyAudio音频输入流
# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=1024)
# # 从sounddevice虚拟声卡中读取音频数据
# audio_data = sd.rec(44100*5, blocking=True)
# # 关闭音频输入流
# stream.close()
# p.terminate()