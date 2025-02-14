import cv2

# pencere olusturma
windowName = "Live Video"
cv2.namedWindow(windowName)

cap = cv2.VideoCapture(0)

print("Width : "+str(cap.get(3)))   # get ile bilgiyi alıyoruz
print("Height : "+str(cap.get(4)))

cap.set(3,1280) # set ile bilgiyi degistiriyoruz
cap.set(4,720)

print("Width* : "+str(cap.get(3)))  # 3 yazıldıgında goruntunun eni 
print("Height* : "+str(cap.get(4)))  # 4 yazıldıgında goruntunun boyu

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)   # y(1) eksenine gore tersi

    cv2.imshow(windowName,frame)

    if cv2.waitKey(1) == 27:    # esc bastıgımda cık
        break

cap.release()
cv2.destroyAllWindows()