import math
import matplotlib.pyplot as plt

ke = 8.99E+09
Q = 8.4E-06
L = 1.9

pdiff = [0 for i in range(0,1000)]
a = [0 for i in range(0,1000)]

for i in range(0,1000):
    a[i] = 2.4+i*0.1

    E_exact = ke*Q/(a[i]*(a[i]+L))
    E_pt_charge = ke*Q/((a[i]+L/2)*(a[i]+L/2))

    pdiff[i] = abs((E_exact-E_pt_charge)/E_exact)
    #print("a = ",a[i]," pdiff = ",pdiff[i])
    if i==0: print ("a = ",a[i]," E = ",E_exact," E_pointcharge = ",E_pt_charge)

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title("Point Charge Approximation")
ax1.set_xlabel('Distance (m)')
ax1.set_ylabel('Fractional Difference')
ax1.grid(True)
#ax1.set_yscale("log",nonposy='clip')
#ax1.set_xscale("log",nonposx='clip')

ax1.scatter(a,pdiff)

plt.show()
