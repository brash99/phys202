from matplotlib import pyplot
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the positions of the charges, the size of the charges, and Coulomb's constant.
#xc = np.array([[1.0,0.0],[0.0,1.0],[-1.0,0.0],[0.0,-1.0]])
#q  = np.array([-1.0E-09,1.0E-09,-1.0E-09,1.0E-09])
#xc = np.array([[1.0,0.0],[0.0,1.0],[-1.0,0.0],[0.0,-1.0]])
#q  = np.array([-1.0E-09,1.0E-09,1.0E-09,-1.0E-09])
xc = np.array([[1.0,0.0],[0.0,1.0],[-1.0,0.0],[0.0,-1.0],[0.7071,-0.7071],[-0.7071,0.7071]])
q  = np.array([1.0E-09,1.0E-09,1.0E-09,1.0E-09,1.0E-09,1.0E-09])
#q  = np.array([-1.0E-09,1.0E-09,1.0E-09,-1.0E-09,1.0E-09,-1.0E-09])
ke = 8.99E+09

# Define the number of points in the x and y directions, and the x and y maximum limits.
npts = 50
xmin = -2.0
xmax = 2.0
ymin = -2.0
ymax = 2.0

# Define arrays to hold the (x,y) positions for the points of interest, and the voltage and each point.
xp = np.arange(xmin,xmax+.001,(xmax-xmin)/(npts-1))
yp = np.arange(ymin,ymax+.001,(ymax-ymin)/(npts-1))
xp, yp = np.meshgrid(xp,yp)

r = [0 for i in range(0,len(xc))]

#print (xp)
#print (yp)

# Loop over number of x and y points of interest (i.e. a grid of npts x npts points).

z = 0
for i in range(0,len(xc)):
    r[i] = np.sqrt((xp-xc[i,0])**2+(yp-xc[i,1])**2)
    z = z + ke*q[i]/r[i]

# Plot the results
fig = pyplot.figure()
ax = fig.gca(projection='3d')

#surf = ax.plot_surface(xp,yp,z,cmap=cm.coolwarm,linewidth=0,antialiased=False)
surf = ax.plot_surface(xp,yp,z)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Voltage (Volts)')
#ax.zaxis._set_scale('log')
ax.set_zlim(-300.0,300.0)
#fig.colorbar(surf,shrink=0.5,aspect=5)
pyplot.show()
