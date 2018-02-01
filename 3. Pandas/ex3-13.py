import pandas as pd

X = pd.read_csv("data_2d.csv", header=None)

# Prints DataFrame
print(type(X))

# Prints the information about the DataFrame
print(X.info())

# Prints first few rows
print(X.head(10))
