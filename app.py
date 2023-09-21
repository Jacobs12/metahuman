# import pyrtmp
# import cv2
# import subprocess

# # 设置摄像头参数
# capture = cv2.VideoCapture(0)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

# # RTMP推流地址
# url = 'rtmp://172.23.0.199:1935/live/stream'
# cmd = ['ffmpeg', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', '640x480', '-i', '-', '-c:v', 'libx264', '-pix_fmt', \
#    'yuv420p', '-preset', 'ultrafast', '-f', 'flv', url]
# p = subprocess.Popen(cmd,stdin=subprocess.PIPE)

# while True:
#     ret, frame = capture.read()
#     if not ret:
#         break
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
#     p.stdin.write(frame.tostring)

# p.communicate()
# p.stdin.close()
# capture.release()

from stream.push_stream import GXStream

if __name__ == '__main__':
    # input = '/Users/admin/Desktop/input.mp4'
    input = '/Users/admin/Desktop/input.mp4'
    output = 'rtmp://172.23.0.199:1935/live/stream'

    stream = GXStream()
    stream.start_stream(input=input,output=output)

# import cv2
# import subprocess as sp

# rtmpUrl = "rtsp://127.0.0.1:1935/stream"
# # camera_path = '/Users/admin/Desktop/input.mp4'
# # cap = cv2.VideoCapture(camera_path)

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

# width = 640
# height = 480
# fps = 30

# # 创建FFmpeg命令行参数 
# command = ['ffmpeg',
#         '-y',
#         '-f', 'rawvideo',
#         '-vcodec','rawvideo',
#         '-pix_fmt', 'bgr24',
#         '-s', "{}x{}".format(width, height),
#         '-r', str(fps),
#         '-i', '-',
#         '-c:v', 'libx264',
#         '-pix_fmt', 'yuv420p',
#         '-preset', 'ultrafast',
#         '-f', 'rtsp',
#         rtmpUrl]

# # 管道配置（这里的作用是用python 启动 ffmpeg.exe命令，如果之前的环境变量配置，不正确。这里无法启动）
# p = sp.Popen(command, stdin=sp.PIPE)

# # read webcamera
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if not ret:
#         print("Opening camera is failed")
#         break

#     p.stdin.write(frame.tobytes())



