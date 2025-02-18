# resimlerdeki gurultuyu azaltma amacı
import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur = cv2.blur(img_filter,(5,5))   # resmin yumusaması(bulanıklasması), 2. arguman pozitif tek sayılar
blur_g = cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)  # 3. arguman sınır cizgisi
blur_m = cv2.medianBlur(img_median,5)   # gurultuyu azaltma
blur_b = cv2.bilateralFilter(img_bilateral,9,95,95) # puturler yok oluyor, resim yumusuyor

cv2.imshow("original",img_bilateral)
cv2.imshow("blur_b",blur_b)


cv2.waitKey(0)
cv2.destroyAllWindows()