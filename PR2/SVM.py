import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 2, 3]
y = [1, 2, 0, 1]

plt.scatter(x[:2], y[:2], color='red', label='+1')
plt.scatter(x[2:], y[2:], color='blue', label='-1')
plt.scatter(1,4,color='red')

xpl= np.linspace(0,5,100)
y1=xpl
y2=xpl-2
plt.plot(xpl, y1, color='red')
plt.plot(xpl, y2, color='blue')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

plt.show()
