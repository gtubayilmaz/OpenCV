import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while 1:

	_,frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # hsv ye cevirdik
	sensitivity = 15    # hassasiyet degeri
	lower_white = np.array([0,0,255-sensitivity])   # beyaz icin en asagı deger
	upper_white = np.array([255,sensitivity,255])   # beyaz icin en ust deger//bu degerleri hazır bulduk=> hsv code for white
	mask = cv2.inRange(hsv,lower_white,upper_white) # lower white ve upper white arasında mask uygula kalanı sil
	res = cv2.bitwise_and(frame,frame,mask=mask)    # ikili bi dongu olustugu icin(framein kendisi ve kazılı frame var) iki kere yazdık
	
	cv2.imshow("frame",frame)
	cv2.imshow("mask",mask)
	cv2.imshow("result",res)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	

cv2.destroyAllWindows()