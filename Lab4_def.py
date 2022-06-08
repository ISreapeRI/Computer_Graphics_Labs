import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

fig = plt.figure()
# точка зрения
Pov = 0
a1 = ((180 - Pov) / 180) * math.pi
b1 = (90 / 180) * math.pi
c1 = ((90 + Pov) / 180) * math.pi

xc1 = 27  # 2,7 см
yc1 = 0
yc2 = yc1 - 1  # вторая камера
zc1 = 0

f = 60  # фокус px
cx = 600  # принцип.точка центр изображения по Ох
cy = 600  # принцип.точка центр изображения по Оy

px = 0.05
py = 0.05

x = 0
y = 0
z = 0
osn = 3
Q = (360 / osn) / 180 * math.pi
osn = osn + 1

sin = math.sin(Q)
cos = math.cos(Q)
Rz1 = np.array([
    [cos, sin, 0, 0],
    [-sin, cos, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

Qz = 0 / 180 * math.pi
sinz = math.sin(Qz)
cosz = math.cos(Qz)
RZ = np.array([
    [cosz, sinz, 0, 0],
    [-sinz, cosz, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

Tv = np.array([[1., 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-x, -y, -z, 1]])
T1v = np.array([[1., 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [x, y, z, 1]])

P = np.array([10, 0, 0, 1])
Ps = np.array([0, 0, 5, 1])

PM = np.append([Ps], [P], axis=0)

for i in range(1, osn - 1):
    P = P.dot(Rz1)
    PM = np.append(PM, [P], axis=0)

PM = PM.dot(RZ)

Rx = np.array([[1, 0, 0],
               [0, math.cos(a1), -math.sin(a1)],
               [0, math.sin(a1), math.cos(a1)]])

Ry = np.array([[math.cos(b1), 0, math.sin(b1)],
               [0, 1, 0],
               [-math.sin(b1), 0, math.cos(b1)]])

Rz = np.array([[math.cos(c1), -math.sin(c1), 0],
               [math.sin(c1), math.cos(c1), 0],
               [0, 0, 1]])

T = np.array([[xc1], [yc1], [zc1]])
T1 = np.array([[xc1], [yc2], [zc1]])

R = Rx.dot(Ry).dot(Rz)
O = np.zeros([1, 3])
O = np.append(O, 1)

C1 = np.append(R, T, axis=1)
C1 = np.vstack([C1, O])

C2 = np.append(R, T1, axis=1)
C2 = np.vstack([C2, O])

e = -R.T.dot(T)
e2 = -R.T.dot(T1)

Cc1 = np.append(R.T, e, axis=1)
Cc1 = np.vstack([Cc1, O])

Cc2 = np.append(R.T, e2, axis=1)
Cc2 = np.vstack([Cc2, O])

K = np.array([[f, 0, cx], [0, f, cx], [0, 0, 1]])
e = np.array(np.eye(3, 3))
e = np.append(e, np.zeros([3, 1]), axis=1)
Pr1 = K.dot(e)

O = np.array([[0], [0], [0], [1]])
Oc = C1.dot(O)

Oc2 = C2.dot(O)

OrtX = np.array([10, 0, 0, 1])  # 27
OrtY = np.array([0, 10, 0, 1])  # 3
OrtZ = np.array([0, 0, 10, 1])  # 22

OrtXc = OrtX.dot(C1.T)
OrtYc = OrtY.dot(C1.T)
OrtZc = OrtZ.dot(C1.T)

II = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
K = np.array([[f / px, 0, cx], [0, f / py, cy], [0, 0, 1]])
Ort_c = K.dot(II)

Ort_c2 = Ort_c.dot(Cc2)
Ort_c = Ort_c.dot(Cc1)

PM1 = Ort_c2.dot(PM.T)
PM = Ort_c.dot(PM.T)

PM[0, :] = PM[0, :] / PM[2, :]
PM[1, :] = PM[1, :] / PM[2, :]
PM[2, :] = PM[2, :] / PM[2, :]

PM1[0, :] = PM1[0, :] / PM1[2, :]
PM1[1, :] = PM1[1, :] / PM1[2, :]
PM1[2, :] = PM1[2, :] / PM1[2, :]

PM = PM.T
PM1 = PM1.T

ax = fig.add_subplot(111)  # 122

P0 = plt.scatter(PM[0, 0], PM[0, 1], color='g')

for i in range(1, osn):
    P0 = plt.scatter(PM[i, 0], PM[i, 1], color='black')
    graph = plt.plot([PM[i, 0], PM[0, 0]], [PM[i, 1], PM[0, 1]], color='r')

plt.fill(PM[1:, 0], PM[1:, 1], 'b', alpha=0.1)

pylab.ylim(600 - 925, 600 + 925)
pylab.xlim(600 - 925, 600 + 925)

if PM1[0, 0] > PM[0, 0]:
    dx = PM1[0, 0] - PM[0, 0]

else:
    dx = PM[0, 0] - PM1[0, 0]

P0 = plt.scatter(PM1[0, 0], PM1[0, 1], color='g')
for i in range(1, osn):
    P0 = plt.scatter(PM1[i, 0], PM1[i, 1], color='black')
    graph = plt.plot([PM1[i, 0], PM1[0, 0]], [PM1[i, 1], PM1[0, 1]], color='r')

    if i == osn - 1:
        graph = plt.plot([PM1[osn - 1, 0], PM1[1, 0]], [PM1[osn - 1, 1], PM1[1, 1]], color='r')
    else:
        graph = plt.plot([PM1[i, 0], PM1[i + 1, 0]], [PM1[i, 1], PM1[i + 1, 1]], color='r')

    plt.fill(PM1[1:, 0], PM1[1:, 1], 'b', alpha=0.1)

plt.show()
