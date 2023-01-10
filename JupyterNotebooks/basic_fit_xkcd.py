import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import signal

#def fitfunction(x,a,b,c,d,e,f,g,h,i):
#    return e*np.sin(d*x+f) + g*np.sin(h*x*x+i) + a*x*x + b*x + c
def fitfunction(x,a,b,c,d):
    return  d*signal.sawtooth(0.2*(x-7.5)) + a*x*x + b*x + c

x = []
y = []

x, y = np.loadtxt('example2.dat', delimiter=',', unpack=True)
xfit = np.linspace(0.5,15.5,num=500)

popt,pcov = curve_fit(fitfunction,x,y)
perr = np.sqrt(np.diag(pcov))

with plt.xkcd():
    plt.scatter(x,y,marker=r'o',label='Experimental Data')
    plt.plot(x,fitfunction(x,*popt),'r-',label='Theory')

    plt.xlabel('Week of the Semester')
    plt.ylabel('Stress Level (Arbitrary Units)')
    plt.title("The End Is In Sight :)")
    plt.legend()
    plt.show()
