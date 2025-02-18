import cv2
import numpy as np

img = cv2.imread("star.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull = cv2.convexHull(cnt, returnPoints = False)    # returnPoints = False oldugunda degerler degil indisleri donuyor
defects = cv2.convexityDefects(cnt,hull)    # kusurları arama

for i in range(defects.shape[0]):   # 0.elemanı kadar donucek
    s, e, f, d = defects[i,0]   # startpoint//endpoint//enuzaknokta(ice bukulmus koseler)//mesafe => 4 deger dondurur
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2) # cizgi cizdik
    cv2.circle(img,far,5,[0,255,0],-1)  # ice donuk noktalar icin

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()