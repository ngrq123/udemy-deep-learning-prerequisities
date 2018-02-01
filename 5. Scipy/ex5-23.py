from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

r = np.random.randn(10000)

plt.hist(r, bins=100)

plt.show()

r = 10 * np.random.randn(10000) + 5

plt.hist(r, bins=100)

plt.show()
