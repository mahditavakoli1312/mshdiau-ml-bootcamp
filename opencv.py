import cv2


img = cv2.imread('Ghossy.jpg')

img[:,:,0] = cv2.multiply(img[:,:,0], 5)
img[:,:,1] = cv2.multiply(img[:,:,1], 5)
img[:,:,2] = cv2.multiply(img[:,:,2], 5)

cv2.imshow("Ghossy", img)
cv2.waitKey(0)

cv2.destroyAllWindows()