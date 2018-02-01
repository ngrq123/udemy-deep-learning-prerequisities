import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = pd.read_csv("data_1d.csv", header=None).as_matrix()

x = A[:,0]
y = A[:,1]

plt.hist(x)

plt.show()

R = np.random.random(10000)

plt.hist(R)

plt.show()

# Buckets
plt.hist(R, bins=20)

plt.show()

y_actual = 2 * x + 1
residuals = y - y_actual

plt.hist(residuals)

plt.show()
