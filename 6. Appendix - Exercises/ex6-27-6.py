import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.random.uniform(low=-1, size=5000)
y = np.random.uniform(low=-1, size=5000)
matrix = np.matrix([x, y]).T

print(matrix)
colors = []
colors_binary = []

for array in matrix:
    x_now = array.item(0, 0)
    y_now = array.item(0, 1)
    if x_now <= 0:
        x_now = False
    else:
        x_now = True

    if y_now <= 0:
        y_now = False
    else:
        y_now = True

    if np.logical_xor(x_now, y_now):
        colors.append('b')
        colors_binary.append(1)
    else:
        colors.append('r')
        colors_binary.append(0)

plt.scatter(x, y, c=colors)

data = pd.DataFrame(matrix)
data['y'] = colors_binary
data.columns = ['x1', 'x2', 'y']
data.to_csv("ex6-27-9.csv")

plt.show()
