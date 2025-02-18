import numpy as np
import matplotlib.pyplot as plt

"""
N = 11
x = np.linspace(0,10,N) # N aralıgında 0 ile 10 arasında deger uretır.

y = x

plt.plot(x,y,"o--")
plt.axis("off") # eksenleri yok eder.
plt.show()
"""
# plot icerisine y girilmeyip sadece x degerleri girilirse indeks deger grafigi olusur.
x = [1,2,3,4]
plt.plot(x,[y**2 for y in x])   # x icerisindeki degerlerin kareleri y degerini olusturcak.
plt.show()