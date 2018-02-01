import numpy as np

A = np.array([[1, 2], [3, 4]])

Ainv = np.linalg.inv(A)
print(Ainv)

# Prints identity matrix
print(Ainv.dot(A))
print(A.dot(Ainv))

print(np.linalg.det(A))

print(np.diag(A))

print(np.diag([1, 2]))

a = np.array([1, 2])
b = np.array([3, 4])

print(np.outer(a, b))
print(np.inner(a, b))

print(a.dot(b))

print(np.diag(A).sum())
print(np.trace(A))

X = np.random.randn(100, 3)
cov = np.cov(X)

print(cov.shape)

cov = np.cov(X.T)

# Eigenvalues and Eigenvectors
# np.eig(C) np.eigh(C)

print(np.linalg.eigh(cov))
print(np.linalg.eig(cov))
