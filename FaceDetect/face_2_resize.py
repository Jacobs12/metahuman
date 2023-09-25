'''
Author: wolffy
Date: 2023-09-25 15:32:57
LastEditors: fengtao92 1440913385@qq.com
LastEditTime: 2023-09-25 16:16:41
FilePath: /metahuman/FaceDetect/face_2_resize.py
Description: 

Copyright (c) 2023 by 北京光线传媒股份有限公司, All Rights Reserved. 
'''

import cv2 as cv
img = cv.imread('FaceDetect/resource/1.jpg')
resize_img = cv.resize(img,dsize=(200,200))
cv.imshow('img',img)
cv.imshow('resize_img',resize_img)
print('修改前：',img.shape)
print('修改后：',resize_img.shape)
while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()
