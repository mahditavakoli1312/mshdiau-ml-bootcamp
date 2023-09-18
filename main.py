import cv2

im = cv2.imread("Cy.jpg")

while(True):
    cv2.imshow("image", im)
    k = cv2.waitKey(5)
    if k == 113:
      break