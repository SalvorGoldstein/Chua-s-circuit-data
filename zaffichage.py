import numpy as np
import matplotlib.pyplot as plt


A=np.loadtxt("chaos.txt",skiprows=1,delimiter=";")
x=A[:,1]
y=A[:,3]
z=A[:,5]



def lissage(d,n):
    d2=np.copy(d)
    for i in range(n,len(d)-1-n,1):
        d2[i]=np.mean(d[i-n:i+n])
    return d2

x=lissage(x,5)
y=lissage(y,5)
z=lissage(z,20)




fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot(x, y, z)

plt.show()































































