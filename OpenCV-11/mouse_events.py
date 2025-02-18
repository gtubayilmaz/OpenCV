import cv2

# faremizle bastıgımız noktada daireler olusturma

cap = cv2.VideoCapture("line.mp4")
circles = []

def mouse(event,x,y,flags,params):  # event ile yapılan hareketi tutucaz, x ve y basılan nokta
    if event==cv2.EVENT_LBUTTONDOWN:    # sol tusa basıldıysa yapılacak islem
        circles.append((x,y))   # basılan noktaları circles icerisine ekliyoruz

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",mouse) # frame uzerine yapılan islemler

while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    for center in circles:  # aldıgımız noktaları cemberlerin merkezi olarak kullanıyoruz
        cv2.circle(frame,center,20,(255,0,0),-1)
        
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key==27:
        break
    elif key == ord("h"):   # h tusuna basıldıgında pencereyi temizler
        circles =[]

cap.release()
cv2.destroyAllWindows()