import cv2
img = cv2.imread('download.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)
edge = cv2.Canny(img,50,100)
cv2.imshow('edges',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
blurred = cv2.GaussianBlur(img , (5,5),0)
cv2.imshow('Blurred',blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
contrastform = img * 1.1
cv2.imshow('Contrast',contrastform)
cv2.waitKey(0)

#cv2.imshow('img',img)
#cv2.waitKey(0)