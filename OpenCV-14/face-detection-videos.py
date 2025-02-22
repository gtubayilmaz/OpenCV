# 1. Kullanacağımız kütüphaneyi çalışmamıza dahil edelim.
import cv2   

# 2. Kullanacağımız videoyu çalışmamıza dahil edelim.
vid = cv2.VideoCapture("faces.mp4")

# 3. Kullanacağımız cascade dosyasını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("D:\\OpenCV\\haarCascade\\frontalface.xml")

#4. Sonsuz bir döngü ile her kareyi(frame) tek tek inceleyelim.
while 1:
    # 5. Her kareyi tek tek okuyalım.
    _, frame = vid.read()
    
    # 6. Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 7. Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinatlarını bulalım.
    faces = face_cascade.detectMultiScale(gray, 1.4, 1)

    # 9. "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    # 10. İşlediğimiz kareleri görelim.
    cv2.imshow('image',frame)

    # 11. Programı kapatacak kodu yazalım.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 12. Son olarak videoyu serbest bırakalım.
vid.release()
cv2.destroyAllWindows()