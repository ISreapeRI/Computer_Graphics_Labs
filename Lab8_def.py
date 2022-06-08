import trimesh
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi
import numpy as np

def update(countOfFrames, x, y, z, plot):
    plot[0].remove()

    if countOfFrames > 20 and countOfFrames <= 42:
        z -= 0.25

    elif countOfFrames <= 20:
        z += 0.25

    plot[0] = ax.plot_trisurf(x, y, z, triangles=triangles, color=(0, 1, 0, 1), alpha=1)

mesh = trimesh.load('./Monkey.obj')
triangles = mesh.faces
nodes = mesh.vertices

x = nodes[:, 0]
y = nodes[:, 2]
z = nodes[:, 1]

section = mesh.section([1, 0, 1], [0, 0, 0])

fig = plt.figure()
ax = fig.gca(projection='3d')

X, Y = np.mgrid[-3:3:10j, -3:3:10j]

Z = X**0 * -1

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0)

ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_zlim(-1,7)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plot= [ax.plot_trisurf(x, y, z, triangles=triangles, color=(0, 1, 0, 1), alpha=1)]

ani = animation.FuncAnimation(fig, update, 46, fargs=(x, y, z, plot), interval=5)

ax.azim = 90
ax.elev = -2

plt.show()