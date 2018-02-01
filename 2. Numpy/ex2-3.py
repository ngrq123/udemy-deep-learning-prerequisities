import numpy as np

L = [1, 2, 3]

A = np.array([1, 2, 3])

for e in L:
    print(e)

L.append(4)

print(L)

# Doesn't work
# A.append(4)

# Adds 5 into the list
L = L + [5]

print(L)

# Doesn't work
# A = A + [4, 5]

# Vector addition
L2 = []
for e in L:
    L2.append(e + e)

print(L2)

# Prints out [2, 4, 6]
print(A + A)


# Plus sign in python list does concatenation,
# but the plus sign in numpy arrays does vector addition

# Print [2, 4, 6]
print(2 * A)

# Prints [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(2 * L)

# Doesn't work, for loop needed
# print(L ** 2)

L2 = []

for e in L:
    L2.append(e * e)

# Prints [1, 4, 9]
print(A ** 2)

# Numpy does calculations without needing a for loop
print(np.sqrt(A))

print(np.log(A))

print(np.exp(A))
