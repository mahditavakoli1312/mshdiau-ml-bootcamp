import cv2
from cv2 import CascadeClassifier

imagePath = 'faces2.jpg'

img = cv2.imread(imagePath)

cascades = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = cascades.detectMultiScale(img,scaleFactor=1.1, minNeighbors=1, maxSize=(100,100))

for(x,y,w,h)in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

cv2.imshow("result",img)
cv2.waitKey(0)