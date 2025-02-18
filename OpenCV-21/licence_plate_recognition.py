import cv2
import numpy as np
import pytesseract
import imutils

img = cv2.imread('licence_plate.jpg')

# plakayı olabildigince ortaya cıkarma islemleri
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filtered = cv2.bilateralFilter(gray, 6, 250, 250)
edged = cv2.Canny(filtered,30,200)

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# uygun konturları yakala
cnts = imutils.grab_contours(contours)
# alana gore 0 dan 10 a kadarını ters sıralama
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screen = None   # kapalı sekil bulup bulamadıgımızı tutucak

for c in cnts:
    epsilon = 0.018*cv2.arcLength(c,True)   # dogruluk katsayısı// arcLength yay uzunlugu bulur
    approx = cv2.approxPolyDP(c,epsilon,True)   # konturları yakınlastırıyor
    if len(approx) == 4:    # 4 kose tespit edildiyse dikdortgen vardır
        screen = approx
        break

mask = np.zeros(gray.shape,np.uint8)
new_img = cv2.drawContours(mask, [screen],0,(255,255,255),-1)
new_img = cv2.bitwise_and(img,img,mask=mask)

(x,y) = np.where(mask == 255)
(topx,topy) = (np.min(x), np.min(y))
(bottomx,bottomy) = (np.max(x), np.max(y))
cropped = gray[topx:bottomx+1, topy:bottomy+1]

text = pytesseract.image_to_string(cropped, lang = "eng")
print(text)

cv2.imshow("img", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
