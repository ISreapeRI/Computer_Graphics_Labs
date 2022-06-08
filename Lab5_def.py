import numpy as np
import matplotlib.pyplot as plt

x = [10, 20, 15, 5]
y = [0, 0, -10, -10]

plt.plot([x[0], x[3]], [y[0], y[3]], 'blue')
plt.plot([x[1], x[2]], [y[1], y[2]], 'blue')

# Матрица формы Берзъе для верхней части

p1 = np.array([
    [x[0], y[0]],
    [x[0] + 2, y[0] + 6],
    [x[1] + 2, y[1] + 4],
    [x[1], y[1]]
])

t = np.linspace(0, 1, 30)

X = []
Y = []

# Матрица Берзье

Mb = np.array([
    [-1, 3, -3, 1],
    [3, -6, 3, 0],
    [-3, 3, 0, 0],
    [1, 0, 0, 0]
])

# Создаем кривую для верхней части фигуры

for i in range(1, len(t)):
    T = np.array([t[i] ** 3, t[i] ** 2, t[i], 1])

    x_ = np.dot(T, np.dot(Mb, p1[:, 0]))
    y_ = np.dot(T, np.dot(Mb, p1[:, 1]))

    X.append(x_)
    Y.append(y_)

# Построение верхней части

plt.plot([x[0], X[0]], [y[0], Y[0]], 'blue')
plt.scatter(X[0], Y[0])

for i in range(1, len(X)):
    plt.plot([X[i - 1], X[i]], [Y[i-1], Y[i]], 'blue')

# Матрица формы Берзъе для нижней части

p2 = np.array([
    [x[2], y[2]],
    [x[2] - 2, y[2] - 6],
    [x[3] - 2, y[3] - 4],
    [x[3], y[3]]
])

# Создаем кривую для нижней части

X = []
Y = []

for i in range(1, len(t)):
    T = np.array([t[i] ** 3, t[i] ** 2, t[i], 1])

    x_ = np.dot(T, np.dot(Mb, p2[:, 0]))
    y_ = np.dot(T, np.dot(Mb, p2[:, 1]))

    X.append(x_)
    Y.append(y_)

# Построение нижней части

plt.plot([x[2], X[0]], [y[2], Y[0]], 'blue')
plt.scatter(X[0], Y[0])

for i in range(1, len(X)):
    plt.plot([X[i - 1], X[i]], [Y[i-1], Y[i]], 'blue')

plt.show()