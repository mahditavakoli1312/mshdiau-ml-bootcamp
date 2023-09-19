import cv2
from matplotlib import pyplot as plt

image = cv2.imread('test.jpg')
cv2.imshow('image',image)
cv2.waitKey(0)

image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',image)
cv2.waitKey(0)

hist= cv2.calcHist(image,[0],None,[256],[0,256])
plt.plot(hist)
plt.title('hist')
plt.xlabel('intensity')
plt.ylabel('pixels')
plt.show()
cv2.waitKey(0)