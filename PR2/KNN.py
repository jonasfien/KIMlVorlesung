import matplotlib.pyplot as plt
import numpy as np

x = [1,1,2,5,6,5]
y = [1,2,1,4,5,5]

plt.scatter(x[:3], y[:3], color='green', label="cluster 1")
plt.scatter(x[3:], y[3:], color='blue' ,label="cluster 2")
xc1=sum(x[:3])/3
xc2=sum(x[3:])/3
yc1=sum(y[:3])/3
yc2=sum(y[3:])/3

plt.scatter(xc1, yc1, color='green')
plt.scatter(xc2, yc2, color='red')
plt.text(xc1,yc1,f"{"%0.2f" % xc1},{"%0.2f" % yc1}")
plt.text(xc2,yc2,f"{"%0.2f" % xc2},{"%0.2f" % yc2}")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

plt.show()
