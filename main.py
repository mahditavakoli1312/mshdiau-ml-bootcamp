import cv2
import matplotlib.pyplot as plt

imgBlack = cv2.imread("Black.jpg")
imgWhite = cv2.imread("White.jpg")

grayBlack = cv2.cvtColor(imgBlack, cv2.COLOR_BGR2GRAY)
grayWhite = cv2.cvtColor(imgWhite, cv2.COLOR_BGR2GRAY)

histB = cv2.calcHist(grayBlack, [0], None, [256], [0,256])
histW = cv2.calcHist(grayWhite, [0], None, [256], [0,256])

plt.subplot(1, 2, 1)
plt.plot(histB)
plt.title('Histogram-Black Image')
plt.xlabel('Intensity')
plt.ylabel('Pixels')

plt.subplot(1, 2, 2)
plt.plot(histW)
plt.title('Histogram-White Image')
plt.xlabel('Intensity')
plt.ylabel('Pixels')
plt.show()