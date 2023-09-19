import cv2

imagePath = "faces.jpg"
img = cv2.imread(imagePath)
cascades = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = cascades.detectMultiScale(img,
                                  scaleFactor=1.1,
                                  minNeighbors=1,
                                  maxSize=(300, 300))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow("result", img)
cv2.waitKey(0)
