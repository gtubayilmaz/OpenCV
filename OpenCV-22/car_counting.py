import cv2
import numpy as np

vid = cv2.VideoCapture("traffic.avi")
backsub = cv2.createBackgroundSubtractorMOG2()
c = 0   # arac sayacı

while True:
    ret,frame = vid.read()
    if ret:
        fgmask = backsub.apply(frame)   # arkaplanı cıkarma uygulaması
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)

        contours,hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try : hierarchy = hierarchy[0]  # hataları gidermek icin
        except: hierarchy=[]

        for contour,hier in zip(contours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)   # contour dan degerlerimizi cekıyoruz
            if w>40 and h >40:  # araba var
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                if x>50 and x<70:
                    c+=1    # bu aralıktan geciyosa sayacı bır artır

        # cv2.putText(source_image,text,coordinates,font,size,color,thickness,better look) 
        # araba sayısını yazdırdık         
        cv2.putText(frame,"car: "+str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
        

        cv2.imshow("Car Counting",frame)
        cv2.imshow("fgmask",fgmask)
        
        if cv2.waitKey(40) & 0xFF==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()      