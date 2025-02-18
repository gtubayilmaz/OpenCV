import numpy as np
import matplotlib.pyplot as plt


path = 'map.jpeg'
img = plt.imread(path)


"""
[r,g,b]
[50,50,0] 50ye 50 deki kırmızı
[70,70,1] 50ye 50 deki yesil
[:,:,2] tum satır ve tum sutunlardaki mavi
r -> 0-255
g -> 0-255
b -> 0-255 
"""

r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

output = np.dstack((r,g,b)) # renkleri ust uste yığ//orjinal resim
plt.imshow(output)
plt.show()



"""
output = [img,r,g,b]
titles = ["Image","Red","Green","Blue"]

for i in range(4):
    plt.subplot(2,2,i+1)    # alt grafikler olusturur, kac satır kac sutun grafigin yerlesicegi yer
    plt.axis("off")
    plt.title(titles[i])
    if i ==0:
        plt.imshow(output[i])   # orjinal resim
    else:
        plt.imshow(output[i],cmap='gray')   # anlasılması kolay olsun diye
    plt.show()


"""
