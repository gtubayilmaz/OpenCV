import numpy as np
import matplotlib.pyplot as plt

path = 'smile.jpg'
img = plt.imread(path)
print(img)
print("min value: ",img.min())  # resmin sayısal en kucuk degeri
print("max value: ", img.max())  # resmin sayısal en buyuk degeri
print("mean: ", img.mean())  # renklerin ortalaması
print("median: ",np.median(img))    # medyan
print("average: ",np.average(img))  # ortalama
print("mean1: ",np.mean(img))   # ortalama