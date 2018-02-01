from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn

# scipy.io.loadmat - used for .mat files
# scipy.io.eavfile.read - used for .wav files
# scipy.signal - convolution functions

x = np.linspace(0, 100, 10000)
y = np.sin(x) + np.sin(3 * x) + np.sin(5 * x)

plt.plot(y)

plt.show()

Y = np.fft.fft(y)

plt.plot(np.abs(Y))

plt.show()

print(2 * np.pi * 16/100)

print(2 * np.pi * 48/100)

print(2 * np.pi * 80/100)
