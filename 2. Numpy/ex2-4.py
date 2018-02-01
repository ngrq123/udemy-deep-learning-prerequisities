import numpy as np

# Vectors

a = np.array([1, 2])

b = np.array([2, 1])

dot = 0

for e, f in zip(a, b):
    dot += e*f

print(dot)

print(a * b)

# Instance method of numpy array
print(np.sum(a * b))

print((a * b).sum())

# Instance method of numpy array
print(np.dot(a, b))

print(a.dot(b))

print(b.dot(a))

amag = np.sqrt((a * a).sum())

print(amag)

amag = np.linalg.norm(a)

print(amag)

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(cosangle)

angle = np.arccos(cosangle)

# In radians
print(angle)
