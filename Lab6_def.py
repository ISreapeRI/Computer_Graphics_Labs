import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource
from Transform import Transform3D

fig = plt.figure()
ax = plt.axes(projection='3d')

ls = LightSource(azdeg=80, altdeg=90)

# Нижняя часть

x = np.array([
    [0., 1.5],
    [3., 1.5]
])

y = np.array([
    [1., 2.],
    [1., 2.]
])

z = x ** 0

rgb = ls.shade(z, plt.cm.Reds)

ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0, facecolors=rgb)

# Верхняя часть

x = np.array([
    [0.75, 1.5],
    [2.25, 1.5]
])

y = np.array([
    [1.25, 1.75],
    [1.25, 1.75]
])

z = x ** 0 * 5

rgb = ls.shade(-z, plt.cm.Reds)

ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0, facecolors=rgb)

# Первая грань

_1 = np.linspace(0, 1.5, 20)
_2 = np.linspace(0.75, 1.5, 20)

X = np.vstack((np.linspace(_1[0], _2[0], 20).T, np.linspace(_1[1], _2[1], 20).T)) # Грань по X

for i in range(2, 20):
    X = np.vstack((X, np.linspace(_1[i], _2[i], 20).T))

_1 = np.linspace(1, 2, 20)
_2 = np.linspace(1.25, 1.75, 20)

Y = np.vstack((np.linspace(_1[0], _2[0], 20).T, np.linspace(_1[1], _2[1], 20).T)) # Грань по Y

for i in range(2, 20):
    Y = np.vstack((Y, np.linspace(_1[i], _2[i], 20).T))

Z = np.vstack((np.linspace(1., 5., 20).T, np.linspace(1., 5., 20).T)) # Грань по Z

for i in range(2, 20):
    Z = np.vstack((Z, np.linspace(1., 5., 20).T))

rgb = ls.shade(-Z, plt.cm.hsv)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, facecolors=rgb)

# Вторая грань

_1 = np.linspace(3, 1.5, 20)
_2 = np.linspace(2.25, 1.5, 20)

X = np.vstack((np.linspace(_1[0], _2[0], 20).T, np.linspace(_1[1], _2[1], 20).T)) # Грань по X

for i in range(2, 20):
    X = np.vstack((X, np.linspace(_1[i], _2[i], 20).T))


_1 = np.linspace(1, 2, 20)
_2 = np.linspace(1.25, 1.75, 20)

Y = np.vstack((np.linspace(_1[0], _2[0], 20).T, np.linspace(_1[1], _2[1], 20).T)) # Грань по Y

for i in range(2, 20):
    Y = np.vstack((Y, np.linspace(_1[i], _2[i], 20).T))


Z = np.vstack((np.linspace(1., 5., 20).T, np.linspace(1., 5., 20).T)) # Грань по Z

for i in range(2, 20):
    Z = np.vstack((Z, np.linspace(1., 5., 20).T))

rgb = ls.shade(-Z, plt.cm.hsv)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, facecolors=rgb)

# Третья грань

_1 = np.linspace(0, 3, 20)
_2 = np.linspace(0.75, 2.25, 20)

X = np.vstack((np.linspace(_1[0], _2[0], 20).T, np.linspace(_1[1], _2[1], 20).T)) # Грань по X

for i in range(2, 20):
    X = np.vstack((X, np.linspace(_1[i], _2[i], 20).T))

Y = np.vstack((np.linspace(1, 1.25, 20).T, np.linspace(1, 1.25, 20).T)) # Грань по Y

for i in range(2, 20):
    Y = np.vstack((Y, np.linspace(1, 1.25, 20).T))

Z = np.vstack((np.linspace(1., 5., 20).T, np.linspace(1., 5., 20).T)) # Грань по Z

for i in range(2, 20):
    Z = np.vstack((Z, np.linspace(1., 5., 20).T))

rgb = ls.shade(-Z, plt.cm.hsv)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, facecolors=rgb)

# Прорисовка

plt.show()
