import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

x, y = np.loadtxt('example.dat', delimiter=',', unpack=True)

plt.scatter(x,y,label='Experimental Data')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Physics 202 Lab 1\nCoulomb's Law")
plt.legend()
plt.show()
