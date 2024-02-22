import cv2
import matplotlib.pyplot as plt

def loadColorImage():
    testColorImage = cv2.imread("original.jpg", 0)
    cv2.imshow("Greyscale converted image", testColorImage)
    return testColorImage


def plotHistogram(testColorImage):
    histogram = cv2.calcHist([testColorImage], [0], None, [256], [0, 256])
    plt.plot(histogram)
    plt.show()

plotHistogram(loadColorImage())
