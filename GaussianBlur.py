import cv2


img = cv2.imread('Ghossy.jpg')

blur = cv2.GaussianBlur(img, (7, 7), 50)

cv2.imshow("Ghossy", blur)
cv2.waitKey(0)

cv2.destroyAllWindows()