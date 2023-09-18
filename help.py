import numpy as np
import cv2


image = cv2.imread('E:\\pictures\\anime\\18840848725573.jpg')


dst = cv2.GaussianBlur(image, (5 , 5) , 0)

cv2.imshow('Fast Means Denoising', dst)
cv2.imshow('original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# #تشخیص لبه
dst = cv2.Canny(image, 50, 150)

cv2.imshow('Fast Means Denoising', dst)
cv2.imshow('original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#کنتراست
dst = cv2.multiply(image, 2.0)

cv2.imshow('Fast Means Denoising', dst)
cv2.imshow('original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()