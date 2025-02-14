import cv2
import numpy as np

img = cv2.imread("helikopter.jpg",0)

kernel = np.ones((5,5),np.uint8)

# resmi erozyona ugratma(bozma)// kernel bozma matrisi// iterasyon tekrar sayısı
erosion = cv2.erode(img, kernel, iterations = 1)

# kalınlastırma
dilation = cv2.dilate(img, kernel, iterations=5)

# gurultuyu kaldırır
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# uyumsuzluk giderme
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# kenarları beyaz yapar
gardient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# icini beyaz yapıyor
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

cv2.imshow("img",img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gardient", gardient)
cv2.imshow("TOPHAT",tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()