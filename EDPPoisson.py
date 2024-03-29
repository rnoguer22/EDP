import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 0
b = np.pi
c = 0
d = np.pi
N = 40
M = 40

w = np.zeros((N+1, M+1))

h = (b - a) / N
k = (d - c) / M

def f(i, j):
    #return (a+h*i)*(c+k*j)*(1-(a+h*i))*(1-(c+k*j))
    return 0

for i in range(1, N):
    w[0][i] = 0
    w[M][i] = 0

for j in range(1, M):
    w[j][0] = c+k*j
    w[j][N] = c+k*j


for _ in range(100):
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = (k**2 * (w[i+1][j] + w[i-1][j]) + h**2 * (w[i][j+1] + w[i][j-1]) - (h*k)**2 * f(i, j)) / (2 * (h**2 + k**2))

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