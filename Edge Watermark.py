import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('C:/Vanya/Research/Dataset/img2.jpg',0)
edges =cv.Canny(img, 100, 200)
image= [img,edges]
location = [121, 122]
for loc, edge_image in zip(location, image):
    plt.subplot(loc)
    plt.imshow(edge_image, cmap='gray')
    cv.imwrite('edge_detected.png', edges)
    plt.savefig('edge_plot.png')
    plt.show()
