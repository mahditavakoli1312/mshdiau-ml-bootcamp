import cv2


image = cv2.imread('faces.jpg')
imageS = cv2.resize(image, (800, 400))
cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = cas.detectMultiScale(imageS, scaleFactor=1.1, minNeighbors=1, minSize=(70, 70))

for(x, y, w, h) in faces:
    cv2.rectangle(imageS, (x,y), (x+w, y+h), (207, 120, 29), 2)

cv2.imshow("People", imageS)
cv2.waitKey(0)

cv2.destroyAllWindows()
