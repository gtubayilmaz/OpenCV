import numpy as np  # numpy kutuphanesini dahil ettik

x = np.array([1,2,3], np.int16)   # np.array ile dizi olusturuyoruz.
# ilk argüman dizi elemanları, ikinci argüman veri tipi

print(type(x))  # <class 'numpy.ndarray'>
print(x[0]);print(x[1]);print(x[2])