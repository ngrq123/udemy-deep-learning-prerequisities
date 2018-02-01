from scipy.stats import norm
import numpy as np

print(norm.pdf(0))

print(norm.pdf(0, loc=5, scale=10))

r = np.random.randn(10)

print(norm.pdf(r))

print(norm.logpdf(r))

print(norm.cdf(r))

print(norm.logcdf(r))
