import cv2


image = cv2.imread('Ghossy.jpg')

cv2.imshow("Ghossy", image)
key = cv2.waitKey(0)