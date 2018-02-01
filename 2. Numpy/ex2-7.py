import numpy as np

print(np.array([1, 2, 3]))

Z = np.zeros(10)
print(Z)

# Tuple in param
Z = np.zeros((10, 10))
print(Z)

ones = np.ones((10,10))
print(ones)

R = np.random.random((10, 10))
print(R)

# Does not work as tuple is not accepted
# G = np.random.randn((10, 10))

G = np.random.randn(10, 10)
print(G)

print(G.mean())

print(G.var())
