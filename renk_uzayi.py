import cv2

img = cv2.imread("klon.jpg")

# cvtColor fonksiyonu ile renk uzayini degistiriyoruz

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # rgb ye donusum
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # hsv ye donusum
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # grayscale e donusum

cv2.imshow("Klon BGR", img) # goruntu bgr durumunda
cv2.imshow("Klon RGB", img_rgb)
cv2.imshow("Klon HSV", img_hsv)
cv2.imshow("Klon GRAY", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
