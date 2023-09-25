import cv2 as cv

img = cv.imread('FaceDetect/resource/1.jpg')
# 灰度
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray_img)
cv.imwrite('FaceDetect/resource/gray_face1.jpg',gray_img)
# 修改尺寸
cv.imshow('FaceDetect/resource/read_img',img)
cv.waitKey(0)
cv.destroyAllWindows()