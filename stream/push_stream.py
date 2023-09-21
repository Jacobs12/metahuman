import subprocess
import pyrtmp

# 推流需要先搭建nigix服务器监听
# MAC：https://www.jianshu.com/p/e5de9dec657b
#         brew tap denji/homebrew-nginx
#         brew install nginx-full --with-rtmp-module
#         brew uninstall nginx-full
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
# ffmpeg安装：conda install ffmpeg-python



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
