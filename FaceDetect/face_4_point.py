'''
Author: wolffy
Date: 2023-09-25 16:15:06
LastEditors: fengtao92 1440913385@qq.com
LastEditTime: 2023-09-25 17:50:56
FilePath: /metahuman/FaceDetect/face_4_point.py
Description: 项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Copyright (c) 2023 by 北京光线传媒股份有限公司, All Rights Reserved. 
'''
import cv2
import numpy as np
import dlib

img_path = 'FaceDetect/resource/1.jpg'

# 加载dlib 人脸检测器
detector = dlib.get_frontal_face_detector()
# 加载dlib人脸关键点
prefictor = dlib.shape_predictor('FaceDetect/Asset/dlib/shape_predictor_68_face_landmarks.dat')
# 读入人脸图片
img = cv2.imread(img_path)
cv2.imshow('img',img)
cv2.waitKey(0)

# 转为灰度图
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray',img_gray)
cv2.waitKey(0)

# 检测人脸
dets = detector(img_gray,1)
# 遍历每张人脸
for face in dets:
    # 获取人脸关键点（对遍历到的这张脸进行关键点检测）
    shape = prefictor(img_gray,face)
    # 获取每个点的坐标，并标记在图片上
    for pt in shape.parts():
        # 转换坐标
        pt_pos = (pt.x,pt.y)
        # 画点
        img_face = cv2.circle(img,pt_pos,1,(0,255,0),2)
    cv2.imshow('face',img_face)
    cv2.waitKey(0)
