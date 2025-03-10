import cv2

vid = cv2.VideoCapture("car.mp4")

car_cascade = cv2.CascadeClassifier("D:\\OpenCV\\car_cascade\\car_cascade.xml")

while 1:
    ret,frame = vid.read()
    frame = cv2.resize(frame, (640,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,2)
    
    for (x,y,w,h) in cars:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow('videos',frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()   