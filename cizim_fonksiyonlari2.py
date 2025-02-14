import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255
#print(canvas)

cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5)    # line ile cizgi cizilir
cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness=7)   # tuval degiskeni, baslangıc, bitis, renk, kalınlık

cv2.rectangle(canvas, (20,20), (50,50), (0,255,0), thickness=-1)    # dikdortgen, sol ust ve sag alt kose, renk, kalınlık
cv2.rectangle(canvas, (50,50), (150,150), (0,255,0), thickness=-1)  # kalınlık = -1 ise ici dolu

cv2.circle(canvas, (250, 250), 100, (0,0,255), thickness=-1)    # cember cizimi// merkez noktası, yarıcap, renk, kalınlık

p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100) # ucgenin 3 noktası

cv2.line(canvas, p1, p2, (0,0,0), 4)
cv2.line(canvas, p2, p3, (0,0,0), 4)
cv2.line(canvas, p1, p3, (0,0,0), 4)    # 3 cizgi ile ucgen cizimi

points = np.array([[[110, 200], [330, 200], [290, 220], [100,100]]], np.int32)
cv2.polylines(canvas, [points], False, (0,0,100), 5)    # cizgileri birlestirir, sekil kapalı olucaksa true

cv2.ellipse(canvas, (300, 300), (100, 50), 0, 0, 360, (255, 255, 0), -1)    # elips olusturur.//merkez noktası,eni,boyu,yatay eksenle yapılıcak açı,baslangıc bitis açıları,renk,kalınlık



cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
