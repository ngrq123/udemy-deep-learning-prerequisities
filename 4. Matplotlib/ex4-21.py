import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
print(df.shape)

M = df.as_matrix()

im = M[0, 1:]
print(im.shape)

im = im.reshape(28, 28)
print(im.shape)

plt.imshow(im)

plt.show()

print(M[0, 0])

plt.imshow(im, cmap='gray')

plt.show()

plt.imshow(255 - im, cmap='gray')

plt.show()
