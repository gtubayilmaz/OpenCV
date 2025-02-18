import numpy as np
import matplotlib.pyplot as plt

path = 'coins.jpg'  # dosya yolu
img = plt.imread(path)  # dosyayı okur
print(img);print("type: ",type(img));print("shape: ",img.shape);print("ndim: ",img.ndim);print("size: ",img.size);print("dtype:", img.dtype)
# verinin tipini, kaca kaclık oldugunu, channel degerini, boyutunu, dtypeını verdi.
print("red channel: ",img[50,50,0]) # rgb--> r =0, g=1, b=2
print("green channel: ",img[50,50,1])   # 50ye 50 pikseldeki yesil
print("blue channel: ",img[50,50,2])
print("rgb channel value: ",img[50,50,:])   # 50ye 50 pikseldeki 3 rengi elde etmek icin