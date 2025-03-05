import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("resim.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=40, param1=100, param2=30, minRadius=30, maxRadius=90)

coin_count = 0

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 3)
        coin_count += 1

cv2.putText(img, f"Bulunan Para Sayisi: {coin_count}", (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("Sonuc", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
