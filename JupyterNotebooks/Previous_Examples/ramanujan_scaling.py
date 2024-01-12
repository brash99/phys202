from scipy.special import factorial
import decimal
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def fitfunction(x,a,b,c):
    return a*x*x + b*x + c

decimal.getcontext().prec = 1001

x = [decimal.Decimal(0) for i in range(0,401)]
y = [decimal.Decimal(0) for i in range(0,401)]

PiDigs = decimal.Decimal(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201983)

Pi = PiDigs/(10**1000)
print ("True value = ",Pi,"\n")

a = decimal.Decimal(26390)
b = decimal.Decimal(1103)
d = decimal.Decimal(8).sqrt()
e = decimal.Decimal(9801)

pisum = decimal.Decimal(0)
for i in range(0,126):
    term1 = decimal.Decimal(factorial(4*i,exact=True))
    term2 = decimal.Decimal(pow(factorial(i,exact=True),4))
    term3 = decimal.Decimal(term1/term2*(a*decimal.Decimal(i)+b)/decimal.Decimal(396**(4*i)))
    pisum = pisum + term3
    pitemp1 = pisum*d/e
    pitemp = decimal.Decimal(1)/pitemp1
    pidiff = abs(pitemp-Pi)
    x.append(i)
    y.append(-decimal.Decimal(1.0)*decimal.Decimal(pidiff).log10())

print(pitemp)

plt.scatter(x,y,label='Scaling Behaviour')

#popt,pcov = curve_fit(fitfunction,x,y)
#perr = np.sqrt(np.diag(pcov))

#plt.plot(x,fitfunction(x,*popt),'r-',label='fit: a=%5.3f +/- %5.3f,\n     b=%5.3f +/- %5.3f,\n     c=%5.3f +/- %5.3f' % (popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))


plt.xlabel('Iteration Number')
plt.ylabel('Number of Decimal Places')
plt.title("Ramanujan's Pi Formula")
plt.legend()
plt.show()


print (x,y)
