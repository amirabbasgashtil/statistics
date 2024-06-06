import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Data.csv')

data = data["data"]

print(data.head())

# average
print('average is ', np.average(data))

# Mean
print('Mean is ', np.mean(data))

# Median
print('Median is ', np.median(data))

# Standard Deviation
print('Standard deviation is ', np.std(data))

# Variance
print('Variance of data is ', np.var(data))

# Histogram
plt.hist(data)
plt.show()