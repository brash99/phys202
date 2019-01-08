import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def fitfunction(x,a,b,c):
    return a*x*x + b*x + c

x = []
y = []

x, y = np.loadtxt('example.dat', delimiter=',', unpack=True)

plt.scatter(x,y,label='Experimental Data')

popt,pcov = curve_fit(fitfunction,x,y)
perr = np.sqrt(np.diag(pcov))

plt.plot(x,fitfunction(x,*popt),'r-',label='fit: a=%5.3f +/- %5.3f,\n     b=%5.3f +/- %5.3f,\n     c=%5.3f +/- %5.3f' % (popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))


plt.xlabel('x')
plt.ylabel('y')
plt.title("Physics 202 Lab 1\nCoulomb's Law")
plt.legend()
plt.show()
