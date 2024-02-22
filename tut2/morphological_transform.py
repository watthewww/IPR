import cv2
import numpy as np 
import matplotlib.pyplot as plt

image_path = 'portrait.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(binary_image, kernel, iterations=1)


dilation = cv2.dilate(binary_image, kernel, iterations=1)

opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

titles = ['Original Binary Image', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [binary_image, erosion, dilation, opening, closing]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()