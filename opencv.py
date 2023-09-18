import cv2


image = cv2.imread('Ghossy.jpg')

while True:
    cv2.imshow("Ghossy", image)

    key = cv2.waitKey(0)
    if key == 27:
        break