import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
e = np.array([11,12,13,14,15,16,17,18,19,20])
y = np.power(x, 2)

##plt.semilogy(x, np.exp(x/5.0), color='lightblue', label='Variance')
plt.grid(True)

plt.errorbar(x, e,color='darkgreen', label='Stanadard Deviation',marker='^')

plt.plot(x, label=('Range:', np.ptp(x)), color='white')

plt.legend()
plt.show()

6
x = np.array([1, 2, 3, 4, 5])
y = np.power(x, 2) # Effectively y = x**2
e = np.array([1.5, 2.6, 3.7, 4.6, 5.5])

plt.errorbar(x, y, e, linestyle='None', marker='^')

plt.show()
