# Define a function which will calculate the new components of the acceleration, based
# on the current position and velocity

# x is a four-component vector that contains the position and velocity components (x and y for each)
# t is the current time
# param is a vector of parameters (in this case, just the gravitational constant times the mass of the Sun)
# deriv is a vector that will contain the new values of the derivatives of the position and velocity
# (i.e. the velocity and acceleration)

import math
from array import array

def gravrk(x,t,param,deriv):
    GM = param[0]
    r1 = x[0]
    r2 = x[1]
    v1 = x[2]
    v2 = x[3]
    normR = math.sqrt(r1*r1+r2*r2)
    accel1 = -GM*r1/(normR*normR*normR)
    accel2 = -GM*r2/(normR*normR*normR)
    deriv[0] = v1
    deriv[1] = v2
    deriv[2] = accel1
    deriv[3] = accel2
def rk4(x, nX, t, tau, deriv, param):
    F1 = array('d')
    F2 = array('d')
    F3 = array('d')
    F4 = array('d')
    xtemp = array('d')

    for i in range(0, nX):
        F1.append(0.0)
        F2.append(0.0)
        F3.append(0.0)
        F4.append(0.0)
        xtemp.append(0.0)

    gravrk(x, t, param, F1)

    half_tau = 0.5 * tau
    t_half = t + half_tau

    for i in range(0, nX):
        xtemp[i] = x[i] + half_tau * F1[i]

    gravrk(xtemp, t_half, param, F2)

    for i in range(0, nX):
        xtemp[i] = x[i] + half_tau * F2[i]

    gravrk(xtemp, t_half, param, F3)

    t_full = t + tau

    for i in range(0, nX):
        xtemp[i] = x[i] + tau * F3[i]

    gravrk(xtemp, t_full, param, F4)

    for i in range(0, nX):
        x[i] = x[i] + tau / 6.0 * (F1[i] + F4[i] + 2.0 * (F2[i] + F3[i]))


def rka(x, nX, t, tau, err, deriv, param):
    tSave = t
    safe1 = 0.9
    safe2 = 0.2

    xSmall = array('d')
    xBig = array('d')
    for i in range(0, nX):
        xSmall.append(0.0)
        xBig.append(0.0)

    maxTry = 100
    for iTry in range(0, maxTry):
        half_tau = 0.5 * tau
        for i in range(0, nX):
            xSmall[i] = x[i]
        rk4(xSmall, nX, tSave, half_tau, deriv, param)
        t = tSave + half_tau
        rk4(xSmall, nX, t, half_tau, deriv, param)

        t = tSave + tau
        for i in range(0, nX):
            xBig[i] = x[i]
        rk4(xBig, nX, tSave, tau, deriv, param)

        errorRatio = 0.0
        eps = 1.0E-16
        for i in range(0, nX):
            scale = err * (math.fabs(xSmall[i]) + math.fabs(xBig[i])) / 2.0
            xDiff = xSmall[i] - xBig[i]
            ratio = math.fabs(xDiff) / (scale + eps)
            if (errorRatio <= ratio):
                errorRatio = ratio

        tau_old = tau
        tau = safe1 * tau_old * math.pow(errorRatio, -0.20)
        if (tau <= tau_old / safe2):
            tau = tau_old / safe2
        if (tau >= safe2 / tau_old):
            tau = safe2 / tau_old

        if (errorRatio < 1):
            for i in range(0, nX):
                x[i] = xSmall[i]
            return

    print("Error:  Adaptive Runge-Kutta Routine failed")

