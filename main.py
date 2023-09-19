import cv2
from cv2 import CascadeClassifier

img = cv2.imread("faces.jpg")
imgR = cv2.resize(img, (400, 200))

cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

coordinates = cas.detectMultiScale(imgR, scaleFactor=1.1, minNeighbors=1, minSize=(30,30))

for(x, y, w, h) in coordinates:
    cv2.rectangle(imgR, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("People", imgR)
cv2.waitKey(0)
cv2.destroyAllWindows()