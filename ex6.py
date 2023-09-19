import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

while 1:
    ret,img = capture.read()
    face = cascade.detectMultiScale(img, scaleFactor=1.01, minNeighbors=10, minSize=(5, 5))
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)

    cv2.imshow('result', img)
    k = cv2.waitKey(1)
    if k == 27:
        break


#face = cascade.detectMultiScale(img, 1.3, 5)
#img = cv2.imread('faces.jpg')
