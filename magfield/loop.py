__author__ = 'wack'

# part of the magwire package

# calculate magnetic fields arising from electrical current through wires of arbitrary shape
# with the law of Biot-Savart

# written by Michael Wack 2015
# wack@geophysik.uni-muenchen.de

# tested with python 3.4.3

# some basic calculations for testing

import numpy as np

import visvis as vv

import wire
import biotsavart


# simple wire
w = wire.Wire(path=wire.Wire.SinusoidalCircularPath(radius=0.5,amplitude=0.0,frequency=12.0,pts=200), discretization_length=0.01,current=2000)
sol = biotsavart.BiotSavart(wire=w)

resolution = 0.1
volume_corner1 = (-0.9, -0.9, -0.9)
volume_corner2 = (0.9, 0.9, 0.9)

grid = np.mgrid[volume_corner1[0]:volume_corner2[0]:resolution, volume_corner1[1]:volume_corner2[1]:resolution, volume_corner1[2]:volume_corner2[2]:resolution]

# create list of grid points
points = np.vstack(map(np.ravel, grid)).T

# calculate B field at given points
B = sol.CalculateB(points=points)

Babs = np.linalg.norm(B, axis=1)

# draw results

# prepare axes
a = vv.gca()
a.cameraType = '3d'
a.daspectAuto = False

vol = Babs.reshape(grid.shape[1:]).T
vol = np.clip(vol, 0.002, 0.01)
vol = vv.Aarray(vol, sampling=(resolution, resolution, resolution), origin=(volume_corner1[2], volume_corner1[1], volume_corner1[0]))

# set labels
vv.xlabel('x axis')
vv.ylabel('y axis')
vv.zlabel('z axis')

sol.vv_PlotWires()

t = vv.volshow2(vol, renderStyle='mip', cm=vv.CM_JET)
vv.colorbar()
app = vv.use()
app.Run()
