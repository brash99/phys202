from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the positions of the charges, the size of the charges, and Coulomb's constant.
x1 = np.array([1.0,0.0])
x2 = np.array([0.0,1.0])
x3 = np.array([-1.0,0.0])
x4 = np.array([0.0,-1.0])
q1 = -1.0E-09
q2 = 1.0E-09
q3 = 1.0E-09
q4 = -1.0E-09
ke = 8.99E+09

# Define the number of points in the x and y directions, and the x and y maximum limits.
npts = 40
xmin = -2.0
xmax = 2.0
ymin = -2.0
ymax = 2.0

# Define arrays to hold the (x,y) positions for the points of interest, and the voltage and each point.
xp = [0 for i in range(0,npts*npts)]
yp = [0 for i in range(0,npts*npts)]
voltage = [0 for i in range(0,npts*npts)]

# Loop over number of x and y points of interest (i.e. a grid of npts x npts points).
for i in range(0,npts):
    for j in range(0,npts):
        index = i*npts+j
        xp[index] = xmin+i/(npts-1)*(xmax-xmin)
        yp[index] = ymin+j/(npts-1)*(ymax-ymin)
        p = np.array([xp[index],yp[index]])

        # calculate the distance from the point of interest to each charge
        d1 = np.sqrt((np.subtract(x1,p)).dot(np.subtract(x1,p)))
        d2 = np.sqrt((np.subtract(x2,p)).dot(np.subtract(x2,p)))
        d3 = np.sqrt((np.subtract(x3,p)).dot(np.subtract(x3,p)))
        d4 = np.sqrt((np.subtract(x4,p)).dot(np.subtract(x4,p)))

        # calculate the voltage at the point of interest
        voltage[i*npts+j] = ke*(q1/d1+q2/d2+q3/d3+q4/d4)

# Plot the results
fig = pyplot.figure()
ax = Axes3D(fig)
ax.scatter(xp,yp,voltage,c='r',marker='o')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Voltage (Volts)')
pyplot.show()
