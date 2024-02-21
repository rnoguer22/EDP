import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 0
b = 1
c = 0
d = 1
N = 100
M = 100

w = [[0 for i in range(N+1)] for j in range(M+1)]

h = (b - a) / N
k = (d - c) / M

def f(x, y):
    return 0

for i in range(N):
    for j in range(M):
        w[i][j] = 0

for i in range(1, N):
    w[i][0] = 0
    w[i][M] = 0

for j in range(1, M):
    w[0][j] = 0
    w[N][j] = 1

for _ in range(100):
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = (k**2 * (w[i+1][j] + w[i-1][j]) + h**2 * (w[i][j+1] + w[i][j-1]) - (h*k)**2 * f(i, j)) / (2 * (h**2 + k**2))

x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)
x, y = np.meshgrid(x, y)

w = np.array(w)  # Convertir la lista de listas a una matriz de NumPy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, w, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()