import cv2
from cv2 import CascadeClassifier

path='faces.JPG'
img =cv2.imread(path)

cascadeClassifier=cv2.CascadeClassifier('1.xml')

faces = cascadeClassifier.detectMultiScale(img,scaleFactor=1.1,minNeighbors=1,maxSize=(60,60))

for(x,y,w,h) in faces : cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)