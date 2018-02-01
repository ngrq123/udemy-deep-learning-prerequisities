from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

r = np.random.randn(10000, 2)

plt.scatter(r[:,0], r[:,1])

plt.show()

r[:,1] = 5 * r[:,1] + 2

plt.scatter(r[:,0], r[:,1])

plt.show()

plt.scatter(r[:,0], r[:,1])

plt.axis('equal')

plt.show()
