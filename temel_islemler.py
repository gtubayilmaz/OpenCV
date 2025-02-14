import cv2
import numpy as np

img = cv2.imread("klon.jpg")

dimension = img.shape
print(dimension)    # resmin boyutları

color = img[420, 500]   # 420ye 500 pikselindeki renk degerlerine erisim
print("BGR: ", color)

blue = img[420, 500, 0] # 420ye 500 pikselindeki mavi renk degerlerine erisim
print("blue: ", blue)

green = img[420, 500, 1]    # 420ye 500 pikselindeki yesil renk degerlerine erisim
print("green: ", green)

red = img[420, 500, 2]  # 420ye 500 pikselindeki kırmızı renk degerlerine erisim
print("red: ", red)

img[420, 500, 0] = 250  # 420ye 500 pikselindeki mavi renk degerini degistirme
print("new blue: ", img[420, 500, 0])

blue1 = img.item(150, 200, 0)   # 150ye 200 pikselindeki mavi degerini item ile alıp degiskene atadık
print("blue1: ", blue1)

img.itemset((150, 200, 0), 172)  # 150ye 200 pikselindeki mavi degerine itemset ile yeni deger atadık
print("new blue1: ", img[150, 200, 0])

cv2.imshow("Klon Asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
