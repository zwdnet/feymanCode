import numpy as np
import matplotlib.pyplot as plt


delta = 0.05
n = int(input('输入模拟步数:'))
x = np.zeros(n)
y = np.zeros(n)
vx = np.zeros(n)
vy = np.zeros(n)
x[0] = 0.5000
vy[0] = 1.6300
r = np.zeros(n)
r[0] = np.sqrt(x[0]**2 + y[0]**2)
ax = np.zeros(n)
ay = np.zeros(n)
ax[0] = -1*x[0]/r[0]**3
ay[0] = -1*y[0]/r[0]**3

for i in range(1, n):
	vx[i] = vx[i-1] + delta*ax[i-1]
	vy[i] = vy[i-1] + delta*ay[i-1]
    #x[i] = x[i-1] + delta*vx[i]
    #y[i] = y[i-1] + delta*vy[i]
    #r[i] = np.sqrt(x[i]**2 + y[i]**2)
    #ax[i] = -1*x[i]/r[i]**3
    
plt.plot(x, y)
plt.savefig('plante.png')
