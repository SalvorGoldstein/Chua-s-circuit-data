import numpy as np
import matplotlib.pyplot as plt


A=np.loadtxt("data.txt",skiprows=1,delimiter=";")

x=A[:,1]
y=A[:,3]
z=A[:,5]

fig = plt.figure()
ax=fig.gca()
ax.plot(x,y,z)
plt.show()































































