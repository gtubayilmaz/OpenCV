import cv2
import numpy as np

img1 = cv2.imread("coins.jpg")
img2 = cv2.imread("balls.jpg")

# gri tona cevirdik
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# gurultu yok ettik
img1_blur = cv2.medianBlur(gray1, 5)
img2_blur = cv2.medianBlur(gray2, 5)

# cemberleri arama:
circles = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1, img1.shape[0]/64, param1=200, param2=10, minRadius=5, maxRadius=30)
# blurlanan resim, algılama metodu, cozunurluk oranı, min mesafe, gradient ve threshold degerleri, min ve maks radius degeri(aralık)