import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('faces.jpg')
face = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, maxSize=(1, 1))
for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)

cv2.imshow('result', img)
cv2.waitKey(0)
