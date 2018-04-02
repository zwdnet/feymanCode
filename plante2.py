import numpy as np
import matplotlib.pyplot as plt

R=[]
d=0.1
x,y=0.500,0.000
vx,vy=0.000,1.630
r=np.sqrt(x**2+y**2)
ax=-(x/r**3)
ay=-(y/r**3)
vx=vx+ax*(d/2)
vy=vy+ay*(d/2)
N = int(input('请输入模拟次数:'))
for t in range(0,N):
	R.append([t/10,x,vx,ax,y,vy,ay,r,1/r**3])
	# print(t/10,x,y)
	plt.scatter(x,y)
	x=x+vx*d
	y=y+vy*d
	r=np.sqrt(x**2+y**2)
	ax=-(x/r**3)
	ay=-(y/r**3)
	vx=vx+ax*d
	vy=vy+ay*d

plt.savefig('plante2.png')
# print(R)