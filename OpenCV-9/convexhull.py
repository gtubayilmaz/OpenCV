import cv2
import numpy as np

img = cv2.imread("map.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = []   # convexhull noktaları tutmak icin bos bir dizi olusturduk

for i in range(len(contours)):  # 0 dan contours uzunluguna kadar 
    hull.append(cv2.convexHull(contours[i],False))  # contours[i] degerinin indisini dondurcek

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)

#   dıs bukey ortu ve konturlerı cizdirme
for i in range(len(contours)):
    cv2.drawContours(bg,contours,i,(255,0,0),3,8, hierarchy)   # 8 => kesintisiz cizgi// hierarchy yazılmasa da olur
    cv2.drawContours(bg,hull,i,(0,255,0),1,8)


cv2.imshow("Image",bg)


cv2.waitKey(0)
cv2.destroyAllWindows()