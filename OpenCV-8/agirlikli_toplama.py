
# f(x,y) = x*a + y*b + c

import numpy as np
import cv2

# resimleri belirli yogunluklarda birbirine eklemek agırlıklı toplamadır.

circle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1) # tam merkezde mavi ici dolu bi cember

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 255), -1)   # ici dolu kırmızı dikdortgen

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)   # circle 0.7 yogunlukta, rectangle 0.3 yogunlukta, sabit sayımız da 0 olucak sekilde ayarladık

cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
