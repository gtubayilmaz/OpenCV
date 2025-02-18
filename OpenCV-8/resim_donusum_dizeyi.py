import cv2
import numpy as np

img = cv2.imread("helikopter.jpg",0)
row,col = img.shape

M= np.float32([[1,0,50],[0,1,100]]) # transformasyon matrisi

dst = cv2.warpAffine(img,M,(row,col))   # kaydırma fonksiyonu

cv2.imshow("dst",dst),

cv2.waitKey(0)
cv2.destroyAllWindows()