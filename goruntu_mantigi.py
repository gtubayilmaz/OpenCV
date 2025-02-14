import cv2
import numpy as np

img = np.zeros((10, 10, 3), np.uint8)   # (10,10) olsaydi siyah beyaz
img[0, 0] = (255, 255, 255) # ilk piksel beyaza boyanır
img[0, 1] = (255, 255, 200)
img[0, 2] = (255, 255, 150)
img[0, 3] = (255, 255, 15)  # mavinin tonları

img = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_AREA)   # yeniden boyutlandırma

cv2.imshow("Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
