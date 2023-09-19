import cv2
import numpy as np
import matplotlib.pyplot as plt

# عکس مشکی
image1 = cv2.imread('b.jpg')

gray_image = cv2.cvtColor(image1, cv2.COLOR_BGRA2GRAY)
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hist = cv2.calcHist([gray_image], [0], None, [256], [0, 255])
cv2.imshow("image", gray_image)

plt.plot(hist)
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("Number of pixels")
plt.show()
cv2.waitKey(0)

#عکس سفید

image2 = cv2.imread('w.jpg')

gray_image = cv2.cvtColor(image2, cv2.COLOR_BGRA2GRAY)
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hist = cv2.calcHist([gray_image], [0], None, [256], [0, 255])
cv2.imshow("image", gray_image)

plt.plot(hist)
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("Number of pixels")
plt.show()
cv2.waitKey(0)