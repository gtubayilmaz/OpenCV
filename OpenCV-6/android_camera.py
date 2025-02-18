import cv2
import numpy as np
import requests

url = "http://192.168.1.21:8080//shot.jpg"

while True:
    img_resp = requests.get(url)    # url yi degiskende tutuyoruz
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)   # aldıgımız goruntuyu dizi icerisinde tutuyoruz
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)   # renkli goruntulenebilir hale getirme
    img = cv2.resize(img, (640,480))    # yeniden boyutlandırma

    cv2.imshow("Android Camera", img)

    if cv2.waitKey(1) == 27:    #
        break

cv2.destroyAllWindows()