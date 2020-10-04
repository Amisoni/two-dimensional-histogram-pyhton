#Two dimensional Histpgram

import cv2
import matplotlib.pyplot as plt


img = cv2.imread('lena.jpg')
HSVImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

HistogramImg = cv2.calcHist([HSVImg], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(HistogramImg, interpolation='nearest')
plt.show()

\
