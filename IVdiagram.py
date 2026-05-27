import numpy as np
import matplotlib.pyplot as plt

nom_fichier ="/home/adam/Documents/study/Chua-s-circuit-data/datas/courbe EI diode"
def lissage(d,n):
    d2=np.copy(d)
    for i in range(n,len(d)-1-n,1):
        d2[i]=np.mean(d[i-n:i+n])
    return d2
A=np.loadtxt(nom_fichier + ".txt",skiprows=1,delimiter=";")
x=A[:,1]
y=A[:,3]


plt.xlabel('V')
plt.ylabel('I')

plt.plot(y,x,linestyle = "none" , marker = "+")
plt.show()
