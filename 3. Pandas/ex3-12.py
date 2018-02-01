import numpy as np

X = []

for line in open("data_2d.csv"):
    row = line.split(",")
    sample = map(float, row)
    X.append(sample)

X = np.array(X)

print(X.shape)
