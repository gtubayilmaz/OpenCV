import cv2
import numpy as np

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

bit_and = cv2.bitwise_and(img2,img1)    # ve islemi
bit_or = cv2.bitwise_or(img2,img1)  # veya islemi
bit_xor = cv2.bitwise_xor(img2,img1)    # xor islemi
bit_not = cv2.bitwise_not(img1) # not islemleri
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow("img2",img2)
cv2.imshow("bit_not",bit_not2)


cv2.waitKey(0)
cv2.destroyAllWindows()