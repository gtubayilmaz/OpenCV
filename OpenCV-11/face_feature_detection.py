import cv2
import numpy as np
import math # matematik kutuphanesi

def findMaxContour(contours):
    max_i = 0
    max_area =0
    for i in range(len(contours)):  # tum konturları gezicek
        area_face = cv2.contourArea(contours[i])    # gezdigi konturların alanını hesaplama ve degiskene atama
        
        if max_area<area_face:
            max_area=area_face
            max_i = i   # max area yı bulma
        try:
            c = contours[max_i]         # c -> maks i indisindeki contours degeri tutuyo      
        except:
            contours = [0]
            c = contours[0] # hata alınırsa c degeri 0 olsun
        return c  # c yi dondurucek


cap  =cv2.VideoCapture(0)


while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    
    #  bolge belirleme 
    roi = frame[50:250,200:400] # frame[y1:y2,x1:x2]
    cv2.rectangle(frame,(200,50),(400,250),(0,0,255),0) # dortgene alma//mask islemine dahil olmasın diye kalınlık 0

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)   # roi yi hsv cevirme
    lower_color = np.array([0,45,79],dtype=np.uint8)
    upper_color = np.array([17,255,255],dtype=np.uint8)

    mask  =cv2.inRange(hsv,lower_color,upper_color)
    
    # temiz goruntu elde etmek icin:
    kernel = np.ones((3,3),np.uint8)
    mask = cv2.dilate(mask,kernel,iterations=1)
    mask = cv2.medianBlur(mask,15)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:   # contours uzunlugu 0 ise;
      
        c = findMaxContour(contours)    # yuz roideki en buyuk (maks) kontur
            
        extLeft = tuple(c[c[:, :, 0].argmin()][0])  # en kucuk x 
        extRight = tuple(c[c[:, :, 0].argmax()][0])     # en buyuk x
        extTop = tuple(c[c[:, :, 1].argmin()][0])   # en kucuk y
        extBot = tuple(c[c[:, :, 1].argmax()][0])   # en buyuk y

        # uc noktalara daire olusturma
        cv2.circle(roi,extLeft,5,(0,255,0),2)
        cv2.circle(roi,extRight,5,(0,255,0),2)
        cv2.circle(roi,extTop,5,(0,255,0),2)
        cv2.circle(roi,extBot,5,(0,255,0),2)

        # noktaları birlestirip cokgen olusturma
        cv2.line(roi,extLeft,extTop,(255,0,0),2)
        cv2.line(roi,extTop,extRight,(255,0,0),2)
        cv2.line(roi,extRight,extBot,(255,0,0),2)
        cv2.line(roi,extBot,extLeft,(255,0,0),2)

        # a b c kenarlarının uzunlugunu hesaplama
        a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1])**2)
        b = math.sqrt((extBot[0]-extRight[0])**2+(extBot[1]-extRight[1])**2)
        c = math.sqrt((extBot[0]-extTop[0])**2+(extBot[1]-extTop[1])**2)

        try:    # 0 a bolme hatasına karsı
            angle_ab= int(math.acos((a**2+b**2-c**2)/(2*b*c))*57)   # açı bulma
            cv2.putText(roi,str(angle_ab),(extRight[0]-100+50,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
        except: # sorun cıkarsa soru isareti
            cv2.putText(roi," ? ",(extRight[0]-100+50,extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
   
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()