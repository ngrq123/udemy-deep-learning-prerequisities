import pandas as pd

X = pd.read_csv("data_2d.csv", header=None)

# Does not work
# X[0, 0]

M = X.as_matrix()
print(type(M))

print(X[0])

print(X.head())

# Numpy X[0] is 0th row
# Pandas X[0] is the column with name 0

# Prints Series
print(type(X[0]))

# Get 1st row
print(X.iloc[0])
print(X.ix[0])

# Prints Series
print(type(X.ix[0]))

# Selects and prints first 2 columns
print(X[[0,2]])

# Prints first column with values less than 5
print(X[X[0] < 5])

# Prints 1d object (series) as booleans
print(X[0] < 5)

print(type(X[0] < 5))
