import cv2
from matplotlib import pyplot as plt 

image_path = 'original.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()

threshold_value = 127
binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')
plt.show()