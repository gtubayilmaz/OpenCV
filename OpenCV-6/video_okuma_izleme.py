import cv2

# video dosyası
cap = cv2.VideoCapture("antalya.mp4")

# webcam
# cap = cv2.VideoCapture(0) # webcam uzerinden video okunacagı zaman 0

while True: # kareleri tek tek okuyup gostersin diye
    ret, frame = cap.read() # frameler dogru okunduysa ret true olur

    if ret == 0:
        break

    # webcam
    # frame = cv2.flip(frame, 1)    # 1 girildiginde frame in y eksenine gore yansıması alınır

    cv2.imshow("Antalya", frame)    # frame goruntuyu aldıgımız degisken
    if cv2.waitKey(10) & 0xFF == ord("q"):  # her bir framei 10 ms ekranda goster ve q ya basarsam pencereyi kapat
        break

cap.release()   # videoyu serbest bırak
cv2.destroyAllWindows()