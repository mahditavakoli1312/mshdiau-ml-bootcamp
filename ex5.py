import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('faces.jpg')
face = cascade.detectMultiScale(img, scaleFactor=1.01, minNeighbors=10, minSize=(5,5 ))
#face = cascade.detectMultiScale(img, 1.3, 5)
for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)

cv2.imshow('result', img)
cv2.waitKey(0)
