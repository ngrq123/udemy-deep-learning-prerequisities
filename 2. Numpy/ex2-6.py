import numpy as np

M = np.array([[1, 2], [3, 4]])
L = [[1, 2], [3, 4]]

print(L[0])
print(L[0][0])

print(M[0][0])
print(M[0, 0])

# Matrix, not recommended
M2 = np.matrix([[1, 2], [3, 4]])
print(M2)

# Convert to numpy array
A = np.array(M2)

# Transpose
print(A.T)
