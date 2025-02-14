import cv2
import numpy as np

img = cv2.imread("text.png")
img1 = cv2.imread("contour.png")

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# koseleri tutacagımız degisken
corners = cv2.goodFeaturesToTrack(gray,1000,0.01,10) # maks kose sayısı//kalite degeri// min mesafe   

corners = np.int8(corners)

for corner in corners:
    x,y = corner.ravel()    # x ve y degerlerini daha rahat alabilmek icin
    cv2.circle(img1,(x,y),3,(0,0,255),-1)   # kırmızı dairelerle belirtiyoruz

cv2.imshow("corner",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()