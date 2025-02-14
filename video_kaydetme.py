import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # cv2.CAP_DSHOW hatadan kurtulmak ıcın

fileName = "webcam.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')  # video uzantısı icin girilen degerler
frameRate = 30
resolution = (640, 480) # cozunurluk

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)   # frameleri dosya haline getir

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)    # frameleri bu degiskene yaz

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()