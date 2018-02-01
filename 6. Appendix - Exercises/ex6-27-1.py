import numpy as np
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt

A = np.array([[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]])
v = np.array([1/3, 1/3, 1/3])

distances = []

for i in range(25):
    v_inv = v.dot(A)
    distances.append(dist.euclidean(v_inv, v))
    v = v_inv

plt.plot(distances)
plt.show()
