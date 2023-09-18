import cv2


img = cv2.imread('Ghossy.jpg')

edge = cv2.Canny(img, 50, 50)

cv2.imshow("Ghossy", edge)
cv2.waitKey(0)

cv2.destroyAllWindows()