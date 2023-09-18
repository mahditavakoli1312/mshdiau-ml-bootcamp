import cv2


image_path="b.png"
image=cv2.imread(image_path)
cv2.imshow("image",image)
cv2.waitkey(0)
cv2.destoryallwindows()