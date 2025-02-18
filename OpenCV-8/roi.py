# roi --> region of interest --> ilgi alanı
import cv2

img = cv2.imread("klon.jpg")
#print(img.shape[:2])   # en ve boy bilgisi

roi = img[30:200, 200:400]  # istedigimiz alanı cıkartıyoruz

cv2.imshow("Klon", img)
cv2.imshow("ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
