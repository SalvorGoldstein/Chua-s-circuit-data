import numpy as np
import matplotlib.pyplot as plt


C1=10e-9
C2=100e-9
L=15e-6
R=2.5e3


R3=2.2e3
R4=22e3
R6=3.3e3

Ga=-1/R3+1/R4
Gb=-1/R3-1/R6
E=15

def g(V):
    return Gb*V+(Ga-Gb)*(abs(V+E)-abs(V-E))/2


def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = ((y-x)/R-g(x))/C1
    y_dot = ((x-y)/R+z)/C2
    z_dot = -y/L
    return np.array([x_dot, y_dot, z_dot])


dt = 1e-8
num_steps = 100000

xyzs = np.empty((num_steps + 1, 3))  # Need one more for the initial values
xyzs[0] = (0., 1., 1.05)  # Set initial values
# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

# Plot
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
