import cv2
import numpy as np

def nothing(x): # bos bir fonksiyon
    pass

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")    # pencere adı

#trackbar olusturuyoruz
cv2.createTrackbar("R", "image", 0, 255, nothing)   # ad, pencere adı, deger aralıgı, bos fonksiyon
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

switch = "0 : OFF, 1 : ON"  # anahtar olusumu
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True: # pencere sureklı yenilensin
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "image")    # konumlarını alıyoruz
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] = [0, 0, 0]  # tum piksel degerleri 0 olsun
    if s == 1:
        img[:] = [b, g, r]  # alınan degerler kullanılsın

cv2.destroyAllWindows()
