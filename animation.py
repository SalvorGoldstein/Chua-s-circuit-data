import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
nom_fichier ="courbe EI diode"
chemin="/home/adam/Documents/study/Chua-s-circuit-data/datas/"
A=np.loadtxt(chemin+ nom_fichier+ ".txt",skiprows=1,delimiter=";")
x=A[:,1]
y=A[:,3]
z=A[:,5]

line, = ax.plot([], [], [])



ax.set_xlabel('Vc1')
ax.set_ylabel('Vc2')
ax.set_zlabel('Il')

STEP = 100      # points added per frame
WINDOW = 800000   # how many points visible at once
    
def update(frame):
    end = frame * STEP
    start = max(0, end - WINDOW)      # trail starts here
    line.set_data(x[start:end], y[start:end])
    line.set_3d_properties(z[start:end])
    return line,

def lissage(d,n):
    d2=np.copy(d)
    for i in range(n,len(d)-1-n,1):
        d2[i]=np.mean(d[i-n:i+n])
    return d2

x=lissage(x,5)
y=lissage(y,5)
z=lissage(z,20)




ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_zlim(min(z), max(z))


ani = animation.FuncAnimation(fig, update, frames=len(x) //STEP, interval=1, blit=False)
#plt.show()


#ani.save((nom_fichier + ".gif, writer="pillow", fps=30)
ani.save(nom_fichier + ".mp4", writer="ffmpeg", fps=30)



























































