import cv2

cv2.namedWindow("Klon", cv2.WINDOW_NORMAL)
img = cv2.imread("klon.jpg")

img = cv2.resize(img, (640,480))    # resmi istedigimiz boyuta ayarlıyoruz

cv2.imshow("Klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()