import numpy as np
import matplotlib.pyplot as plt

n = 1000

y = []

for i in range(1000):
    x = np.random.uniform(size=n).sum()
    y.append(x)

y = np.array(y)

plt.hist(y)

plt.show()
