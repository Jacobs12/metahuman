'''
Author: wolffy
Date: 2023-09-21 10:16:32
LastEditors: fengtao92 1440913385@qq.com
LastEditTime: 2023-11-02 11:05:09
FilePath: /metahuman/stream/push_stream.py
Description: 项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Copyright (c) 2023 by 北京光线传媒股份有限公司, All Rights Reserved. 
'''
import subprocess
import pyrtmp

# 推流需要先搭建nigix服务器监听
# MAC：https://www.jianshu.com/p/e5de9dec657b
#         brew tap denji/homebrew-nginx
#         brew install nginx-full --with-rtmp-module
#         如果报错了就brew uninstall nginx-full
#         打开文件/usr/local/etc/nginx/nginx.conf，编辑文件，在最下边添加如下rtmp配置
# rtmp {
#     server {
#         listen 1935;
#         ping 30s;
#         notify_method get;

#         application live {
#             live on;
#             record off;
#         max_connections 1024;
#         }
#         }
# }
# /usr/local/Cellar/nginx-full/1.19.0/bin/nginx -s reload
# nginx
# 在浏览器里打开http://localhost:8080
# $ nginx -s quit
# 或者
# $ nginx -s stop
# ffmpeg安装：conda install ffmpeg


# OBS 服务器：rtmp://172.23.0.199/live 推流码:stream 接收:rtmp://172.23.0.199/live/stream

class GXStream(object):
    def __init__(self) -> None:
        print('')
    
    def start_stream(self,input : str,output : str):
        # # RTMP推流地址
        url = output
        cmd = ["ffmpeg", "-re", "-i", input,"-vcodec", "h264", \
               "-preset","superfast", "-acodec","aac", "-strict", "experimental", "-f", "flv",url]
        print(' '.join(cmd))
        p = subprocess.Popen(cmd,stdin=subprocess.PIPE)

# 转发直播流
    def relay_stream(self,input:str,output:str):

        cmd = ["ffmpeg","-re","-i",input, "-vcodec", "copy", "-acodec", "aac", "-b:a", "192k", "-b:v", "3000k", "-f", "flv", output]
        p = subprocess.Popen(cmd,stdin=subprocess.PIPE)
