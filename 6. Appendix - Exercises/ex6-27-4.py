import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")
grouped_data = data.groupby(['label']).mean()
print(grouped_data)

grouped_data = grouped_data.as_matrix()

for i in range(10):
    im = grouped_data[i, :]
    im = im.reshape(28, 28)
    im = np.rot90(im, axes=(1,0))
    plt.imshow(im)
    plt.show()
