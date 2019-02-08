nsteps = 100000
a = 2.4
ke = 8.99E+09
Q = 8.4E-06
L = 1.9

E_total = 0.0

dx = 1.0*L/nsteps
dq = Q*dx/L

for i in range(0,nsteps):
    x = -1.0*L+i*dx
    dE = ke*dq/((a-x)*(a-x))
    E_total = E_total + dE

print ("E_total = ",E_total)
E_exact = ke*Q/(a*(a+L))
print ("E_exact = ",E_exact)

