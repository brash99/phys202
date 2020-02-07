__author__ = 'wack'

# part of the magwire package

# calculate magnetic fields arising from electrical current through wires of arbitrary shape
# with the law of Biot-Savart

# written by Michael Wack 2015
# wack@geophysik.uni-muenchen.de

# tested with python 3.4.3

# some basic calculations for testing

import numpy as np
import matplotlib.pyplot as plt

import wire
import biotsavart


# simple wire
#w = wire.Wire(path=wire.Wire.SolenoidPath(), discretization_length=0.01, current=100).Translate((0.0, 0.0, 0.0)).Rotate(axis=(1.0, 0.0, 0.0), deg=0.0)
w = wire.Wire(path=wire.Wire.LinearPath([0.5,0.5,0.0],[0.5,0.5,1.0],pts=200), discretization_length=0.01, current=1000000)
sol = biotsavart.BiotSavart(wire=w)

resolution = 0.1
volume_corner1 = (.2, .2, .2)
volume_corner2 = (.8, .8, .8)

grid = np.mgrid[volume_corner1[0]:volume_corner2[0]:resolution, volume_corner1[1]:volume_corner2[1]:resolution, volume_corner1[2]:volume_corner2[2]:resolution]

# create list of grid points
points = np.vstack(map(np.ravel, grid)).T

# calculate B field at given points
B = sol.CalculateB(points=points)

Babs = np.linalg.norm(B, axis=1)

#Draw results
# remove big values close to the wire
cutoff = 4.0
minvalue = 0.0002

B[Babs > cutoff] = [np.nan,np.nan,np.nan]
B[Babs < minvalue] = [np.nan,np.nan,np.nan]

fig = plt.figure()
# 3d quiver
ax = fig.gca(projection='3d')
sol.mpl3d_PlotWires(ax)
ax.quiver(points[:, 0], points[:, 1], points[:, 2], B[:, 0], B[:, 1], B[:, 2], length=0.04)
plt.show()

