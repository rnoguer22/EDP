import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 0
b = 5
c = 0
d = 10
N = 40
M = 400

w = np.zeros((M+1, N+1))

h = (b - a) / N
k = (d - c) / M

v = 1.5

p = v*k/h #Longitud de la cuerda


def f(x):
    return x*(b-x)

def g(x):
    return 0

for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

for i in range(1, N):
    w[0][i] = f(h*i)
    w[1][i] = w[0][i] + k*g(h*i)


for j in range(1, M):
    for i in range(1, N):
        w[j+1][i] = 2*(1-((v*k/h)**2)) * w[j][i] + ((v*k/h)**2) * (w[j][i+1] + w[j][i-1]) - w[j-1][i] 

x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)
x, y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(y, x, w, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()