import matplotlib.pyplot as plt

qtot = 2.0E-06
d = 1.0
k = 8.99E+09

force = [0.0 for i in range(0,1000)]
q1 = [0.0 for i in range(0,1000)]

for i in range(0,1000):
    q1[i] = 1.0*i/999.0*qtot
    q2 = qtot - q1[i]
    force[i] = k*q1[i]*q2/(d*d)
    print(i,q1[i],q2,force[i])

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(q1,force)

ax1.set_title("Charge Splitting")
ax1.set_xlabel('q1 (C)')
ax1.set_ylabel('Force (N)')
ax1.grid(True)

plt.show()

