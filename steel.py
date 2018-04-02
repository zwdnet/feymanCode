import numpy as np
import matplotlib.pyplot as plt


n = int(input('请输入计算次数:'))
x = np.zeros(n)
delta = 0.1
v = np.zeros(n)
x[0] = 1.0
a = np.zeros(n)

for i in range(1, n):
	a[i] = -1*x[i-1]
	v[i] = v[i-1] + delta*a[i]
	v[1] = v[0] + 0.5*delta*a[0]
	x[i] = x[i-1] + delta*v[i]
	
plt.subplot(3, 1, 1)
plt.plot(x, '*-')
plt.ylabel('x')
plt.subplot(3, 1, 2)
plt.plot(v, 'o-')
plt.ylabel('v')
plt.subplot(3, 1, 3)
plt.plot(a, '.-')
plt.ylabel('a')
plt.savefig('steel.png')

