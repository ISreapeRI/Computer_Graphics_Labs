import numpy as np
import matplotlib.pyplot as plt

point = [1, 1, 0, 1]

Qx = 60 / 180 * np.pi

Rx = np.array([[1, 0, 0, 0],
               [0, np.cos(Qx), np.sin(Qx), 0],
               [0, -np.sin(Qx), np.cos(Qx), 0],
               [0, 0, 0, 1]])

T = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, -10, 1]])

Tz = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 10, 1]])

Q = [i / 180 * np.pi for i in np.linspace(0, 360, 256)]

Rz = [np.array([[np.cos(q), np.sin(q), 0, 0],
               [-np.sin(q), np.cos(q), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]) for q in Q]

M = np.dot(np.dot(T, Rx), Tz)

down_vertex = np.array([np.dot(point, r) for r in Rz])
print(down_vertex.shape)
upper_vertex = np.dot(np.dot(down_vertex, Tz), M)

ax = plt.axes(projection = '3d')
[ax.plot([down_vertex[i][0], upper_vertex[i][0]],
         [down_vertex[i][1], upper_vertex[i][1]],
         [down_vertex[i][2], upper_vertex[i][2]], 'blue') for i in range(len(down_vertex))]

ax.view_init(5, 0)

plt.show()