import numpy as np

matrix = np.array([[1, 2], [2, 1]])
print(np.allclose(matrix, matrix.T))
