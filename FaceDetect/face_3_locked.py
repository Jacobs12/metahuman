import cv2 as cv

img = cv.imread('FaceDetect/resource/1.jpg')

def face_detect_demo():
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('FaceDetect/Asset/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

face_detect_demo()
while True:
    if ord('q') == cv.waitKey(0):
        break
    cv.destroyAllWindows()
    