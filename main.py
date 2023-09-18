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


# خواندن تصویر
image = cv2.imread('sib.jpg', cv2.IMREAD_GRAYSCALE)  # تبدیل تصویر به سیاه و سفید

# اعمال فیلتر سوبل
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)  # تشخیص لبه‌های افقی
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)  # تشخیص لبه‌های عمودی

# محاسبه مقدار جمعی از مقادیر سوبل افقی و عمودی
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# نمایش تصویر حاصل
cv2.imshow('Edge Detection (Sobel)', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

# خواندن تصویر
image = cv2.imread('sib.jpg')

# تبدیل تصویر به سیاه و سفید
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# اعمال تبدیل لاپلاسیان
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

# تعیین مقیاس افزایش کنتراست
alpha = 1.5  # مقیاس افزایش کنتراست (می‌توانید مقدار دلخواه خود را انتخاب کنید)

# محاسبه تصویر نهایی با افزایش کنتراست
contrast_image = cv2.convertScaleAbs(laplacian, alpha=alpha)

# نمایش تصویر حاصل
cv2.imshow('Original Image', image)
cv2.imshow('Contrast Enhanced Image', contrast_image)
cv2.waitKey(0)
cv2.destroyAllWindows()\