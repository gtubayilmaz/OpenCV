import cv2

vid = cv2.VideoCapture("eye_motion.mp4")

while 1:
    ret,frame=vid.read()
    if ret is False:
        break

    roi = frame[80:210,230:450] # gozu roi olarak belirleme
    rows,cols,_ = roi.shape
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    _,threshold = cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)   # THRESH_BINARY_INV ile siyah olan yeri beyaz yaptık

    # goz bebeginin konturlarını bulma
    contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # kontur degerlerini sıralama, key ile neye gore sıralama yapıcagını belirtiyoruz, burda alana gore sıralıyor
    contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse=True)   # reverse true ise buyukten kucuge sırala

    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)   # dort koordinat degeri dondurur
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)  # dikdortgen cizimi

        # iki dogru cizdik
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)  # dikey
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)  # yatay
        break
    
    frame[80:210,230:450] = roi # frame uzerine roi ekleme
    
    cv2.imshow("frame",frame)
  
    if cv2.waitKey(80) & 0xFF==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()