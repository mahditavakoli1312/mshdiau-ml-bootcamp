import cv2
import matplotlib.pyplot as plt


black_img = cv2.imread('Ghossy.jpg')
black_img = cv2.cvtColor(black_img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist(black_img, [0], None, [256], [0, 256])

plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Intensity')
plt.ylabel('Brightness')
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()