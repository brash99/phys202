from scipy.special import factorial
import decimal

decimal.getcontext().prec = 1001

a = decimal.Decimal(26390)
b = decimal.Decimal(1103)
d = decimal.Decimal(8).sqrt()
e = decimal.Decimal(9801)

pisum = decimal.Decimal(0)
for i in range(0,401):
    term1 = decimal.Decimal(factorial(4*i,exact=True))
    term2 = decimal.Decimal(pow(factorial(i,exact=True),4))
    term3 = decimal.Decimal(term1/term2*(a*decimal.Decimal(i)+b)/decimal.Decimal(396**(4*i)))
    pisum = pisum + term3
    pitemp1 = pisum*d/e
    pitemp = decimal.Decimal(1)/pitemp1

print(pitemp)
