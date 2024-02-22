import cv2
import matplotlib.pyplot as plt

# Read the original image
img = cv2.imread('original.jpg') 

 
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

 
# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

title = ['Original', 'Sobel X', 'Sobel Y', "Sobel X Y", 'Canny Edge Detection']
images = [img_gray, sobelx, sobely, sobelxy, edges]
for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
