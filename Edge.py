import cv2

img = cv2.imread("Cy.jpg")
edg = cv2.Canny(img, 150, 100)

cv2.imshow("Edge" , edg)

cv2.waitKey(0)
cv2.destroyAllWindows()

