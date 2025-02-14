import cv2

img = cv2.imread("klon.jpg",0)  # resimlerin matematiksel degerlerini okur
#  print(img) --> resmin matematiksel degerlerini yazdırır.
cv2.namedWindow("image",cv2.WINDOW_NORMAL)  # pencereyi buyutup kucultme ozelligi

cv2.imshow("image",img) # resmin yerlesicegi pencere ve resmin tutuldugu degisken
cv2.imwrite("klon1.jpg",img)    # klon1 e kaydet
cv2.waitKey(0)  # pencereyi kapatana kadar resmi gormek icin
cv2.destroyAllWindows() # pencerelerin tumunu kapatır