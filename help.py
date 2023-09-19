from matplotlib import pyplot as mt
import cv2

image = cv2.imread('E:\\u\\python\\hello\\black.jpg')
image2 = cv2.imread('E:\\u\\python\\hello\\white.jpg')
cv2.imshow('image', image )
hist=cv2.calcHist([image],[0],None,[256],[0,256])
# hist2=cv2.calcHist([image2],[0],None,[256],[0,255])
# mt.plot(hist)
# mt.title('histogram')
# mt.xlabel('intensity')
# mt.ylabel('num of pixels')
# mt.show()
mt.plot(hist)
mt.title('histogram')
mt.xlabel('intensity')
mt.ylabel('num of pixels')
mt.show()
cv2.waitKey(0)