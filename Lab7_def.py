import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import trimesh

mesh = trimesh.load('./Monkey.obj')
triangles = mesh.faces
nodes = mesh.vertices

x = nodes[:, 0]
y = nodes[:, 2]
z = nodes[:, 1]

# Section mesh by an arbitrary plane defined by its normal vector and origin
section = mesh.section([1, 0, 1], [0, 0, 0])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(x, y, z, triangles=triangles, color=(0, 1, 0, 1), alpha=1)

X, Y = np.mgrid[-3:3:10j, -3:3:10j]

Z = X**0 * -1

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0)

ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_zlim(-1,1)

plt.show()
