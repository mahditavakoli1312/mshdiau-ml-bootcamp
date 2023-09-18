import cv2

img = cv2.imread("Cy.jpg")

imB = cv2.GaussianBlur(img , (9, 9), 40)

cv2.imshow("Blur" , imB)
cv2.waitKey(0)
cv2.destroyAllWindows()