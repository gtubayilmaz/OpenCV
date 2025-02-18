# ndarray --> n-dimensional array --> n boyutlu dizi

import numpy as np
x = np.array([[-2,-1,0,5],[9,4,5,-7],[9,7,6,5]],np.int16) # unsigned int = isaretsiz sayılar(negatif sayılar yok)

print(x)

print(x.shape)
print(x.ndim)
print(x.dtype)
print(x.size)
print(x.T)