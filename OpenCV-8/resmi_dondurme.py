import cv2
import numpy as np

img = cv2.imread("helikopter.jpg",0)
row,col = img.shape

M= cv2.getRotationMatrix2D((col/5,row/3),180,1) # 2 boyutta yon degistirme// sutun satır açı ve olcek

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()