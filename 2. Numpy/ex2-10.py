import numpy as np

# Ax = b
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])

x = np.linalg.inv(A).dot(b)

print(x)

x = np.linalg.solve(A, b)

print(x)
