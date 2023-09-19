import cv2
from cv2 import CascadeClassifier
image = cv2.imread('E:\\u\\python\\hello\\1920_stock-photo-mosaic-of-satisfied-people-157248584.jpg')
cascode = cv2.CascadeClassifier('E:\\u\\python\\hello\\haarcascade_frontalface_default.xml')
happy_face =cascode.detectMultiScale(image , scaleFactor=1.1,minNeighbors=15,maxSize=(150,150))
for (x,y,w,h) in happy_face:
    cv2.rectangle(image,(x,y),(x+w , y+h),(0,0,255),3)
cv2.imshow('happy face',image)
cv2.waitKey(0)