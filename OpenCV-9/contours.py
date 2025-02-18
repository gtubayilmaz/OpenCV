import cv2

img = cv2.imread('contour1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # gray moda cevirdik

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  # threshold uyguladık 

# ilk arguman icin koordinatları bulucak//son iki arguman konturleme islemini kolaylastırır
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # _ degiskenlerini kullanmıcaz
print(contours)
