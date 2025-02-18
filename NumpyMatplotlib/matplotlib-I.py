import matplotlib.pyplot as plt # matplotlib icerisinden pyplot dahil ediyoruz
import numpy as np

x = np.arange(5) # 5 e kadar sayı uretir
y = x

plt.plot(x,y,"o--")  # plot ile grafik cizilir
plt.plot(x,-y)
plt.plot(-x,y,"o")  # o, o-, o-- # 3. arguman grafigin nasıl cizilicegini soyler.
plt.title("y=x, y=-x")  # grafigin adı girilir.
plt.show()  # show ile grafik gosterilir