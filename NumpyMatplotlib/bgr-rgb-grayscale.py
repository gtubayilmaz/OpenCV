import cv2
import matplotlib.pyplot as plt

path = "smile.jpg"
img = cv2.imread(path,0) # 1 oldugunda BGR formatta okur, 0 yazarsak grayscale okur.
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # BGR RGB e cevrilir.
plt.imshow(img,cmap='gray',interpolation = 'BICUBIC') # imshow RGB ile gosterir
# cmap resmin renk haritası, bozulmayı duzeltmek icin interpolation
plt.show()