import cv2
p= cv2.imread('test.jpg')
nc= cv2.GaussianBlur(p,(5,5),0)
cv2.imshow('nc',nc)
cv2.waitKey(0)
canny=cv2.Canny(p,150,100)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cont=p
cont[:,:,2]=cont[:,:,2]+50
cont[:,:,1]=cont[:,:,1]+50
cont[:,:,0]=cont[:,:,0]+50
cv2.imshow('cont',cont)
cv2.waitKey(0)