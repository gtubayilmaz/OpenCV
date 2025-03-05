import cv2
import numpy as np

def process_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (480, 480), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Kenar tespiti
    edges = cv2.Canny(blur, 50, 150)

    # Morfolojik işlemler ile gürültü azaltma
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(edges, cv2.MORPH_OPEN, kernel, iterations=2)

    # Arka plan belirleme
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Mesafe dönüşümü ve ön plan belirleme
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

    # Bilinmeyen bölge
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Nesneleri etiketleme
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    # Watershed uygulama
    cv2.watershed(img, markers)
    img[markers == -1] = [0, 0, 255]  # Kenarları kırmızı çiz

    # Çember tespiti için HoughCircles kullanımı
    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT, 1.2, 30,
        param1=100,  # Kenar algılama için eşik
        param2=80,   # Çember tespiti eşik değeri (daha yüksek yap)
        minRadius=20,  # Küçük çemberleri hariç tut
        maxRadius=90   # Büyük çemberleri hariç tut
    )

    count = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        count = len(circles[0])
        for i in circles[0, :]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Yeşil çember
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)  # Merkez noktası

    cv2.putText(img, f"Bulunan Para Sayisi: {count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    

    # Sonucu göster
    cv2.imshow('Tespit Edilen Cemberler', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Kullanım
image_path = "resim1.jpg"
process_image(image_path)
