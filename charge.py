import numpy as np
import math
import matplotlib.pyplot as plt

ke = 8.99E+09
q1 = 5.8E-06
q2 = 16.8E-06

l1 = 1.0
l2 = 1.0
pdiff = [0 for i in range(0,1000)]
a = [0 for i in range(0,1000)]

for i in range(0,1000):
    a[i] = 1.0+i*0.1

    fraction = (a[i]+l1)*(a[i]+l2)/((a[i])*(a[i]+l1+l2))
    f12 = ke*q1*q2*math.log(fraction)/(l1*l2)
    f12_pt_charge = ke*q1*q2/((a[i]+l1/2+l2/2)*(a[i]+l1/2+l2/2))

    pdiff[i] = abs((f12-f12_pt_charge)/f12)
    #print("a = ",a[i]," pdiff = ",pdiff[i])
    #print ("a = ",a," Force = ",f12," Force_pointcharge = ",f12_pt_charge)

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title("Point Charge Approximation")
ax1.set_xlabel('Distance (m)')
ax1.set_ylabel('Fractional Difference')
ax1.grid(True)
ax1.set_yscale("log",nonposy='clip')
ax1.set_xscale("log",nonposx='clip')

ax1.scatter(a,pdiff)

plt.show()
