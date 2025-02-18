import cv2
import numpy as np

image_path = "starwars.jpg"
template_path = "starwars2.jpg"

# gray e cevirme
img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# gray okuma
template = cv2.imread(template_path,cv2.IMREAD_GRAYSCALE)
w,h = template.shape[::-1]  # template in genislik ve yuksekligi

# matchTemplate ile resim eslestirme//sablonun yerlestirilcegi resim//sablon//sabit
result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
location = np.where(result >= 0.95) # ne kadar 1 e yakınsa sablon orda// 1 e yakın koordinatları dondurucek


for point in zip(*location[::-1]):  # location daki noktaların yukseklik ve genislik degerleri
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),3)    # dikdortgen cizimi


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()