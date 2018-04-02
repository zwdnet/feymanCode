import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


n = int(input('请输入模拟次数:'))
distance = np.zeros(n)
step = np.random.randint(2,size=n)
z = np.zeros(n)

for i in range(1, n):
	if step[i] == 1:
	    distance[i] = distance[i-1] + step[i]
	else:
		distance[i] = distance[i-1] - 1
	z[i] = np.sqrt(i)
dis = np.sqrt(distance**2)
x = np.linspace(1, n, n)
plt.plot(x, dis, x, z)
plt.savefig( 'walk.png')
