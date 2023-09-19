import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('white.jpg')
NewImg1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
hist1 = cv2.calcHist(NewImg1,[0],None,[256],[0,256])

img2 = cv2.imread('black.jpg')
NewImg2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
hist2 = cv2.calcHist(NewImg2,[0],None,[256],[0,256])

plt.plot(hist1)
plt.title('histogram(white)')
plt.xlabel("intensity")
plt.ylabel('pixels')
plt.show()
plt.plot(hist2)
plt.title('histogram(black)')
plt.xlabel("intensity")
plt.ylabel('pixels')
plt.show()
