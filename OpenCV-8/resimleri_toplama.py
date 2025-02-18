import numpy as np
import cv2

# resimler birer matrislerdir, toplama islemi yapılabilmesi icin aynı boyutta olmaları gerekir

circle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1) # tam merkezde mavi ici dolu bi cember

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 255), -1)   # ici dolu kırmızı dikdortgen

add = cv2.add(circle, rectangle)    # resimleri toplama fonksiyonu
print(add[256, 256])    # 256x256 daki toplanmıs degerler [255   0 255]

cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Add", add)

cv2.waitKey(0)
cv2.destroyAllWindows()
