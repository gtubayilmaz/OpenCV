import cv2

img = cv2.imread("starwars.jpg")
blurry_img = cv2.medianBlur(img,9)  # resmin bulanık hali

laplacian= cv2.Laplacian(blurry_img,cv2.CV_64F).var()   # burdan donen degere gore blurlu olup olmadıgını anlıcaz
print(laplacian)

if laplacian < 500: # deger 500 den kucukse blurlu
    print("blurry image")


cv2.imshow("img",img)
cv2.imshow("blurry_img",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()