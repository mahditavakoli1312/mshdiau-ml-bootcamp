import cv2
import numpy as np

# خواندن تصویر
image = cv2.imread('download.jpeg')

# اعمال فیلتر میانگین با اندازه مشخص
kernel_size = 5  # اندازه فیلتر میانگین
denoised_image = cv2.blur(image, (kernel_size, kernel_size))

# نمایش تصویر حاصل
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
