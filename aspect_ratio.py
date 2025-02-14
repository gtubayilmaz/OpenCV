import cv2

def resizewithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):
    
    dimension = None    # yeni boyut
    (h,w) = img.shape[:2]   # boy ve en bilgisini aldık

    if width is None and height is None:
        return img  # resmin orjinalini dondurur
    
    if width is None:   # girilen boy degerine gore hesaplanıcak
        r = height / float(h)   # hassas hesaplama icin float
        dimension = (int(w*r), height)

    else: # girilen en degerine gore hesaplanıcak
        r = width / float(w)
        dimension = (width, int(h*r))

    return cv2.resize(img, dimension, interpolation = inter)

img = cv2.imread("klon.jpg")
img1 = resizewithAspectRatio(img, width = None, height = 600, inter = cv2.INTER_AREA)
#600 boy degerine gore en hesaplandı ve resim boyutlandırıldı
cv2.imshow("Original", img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()