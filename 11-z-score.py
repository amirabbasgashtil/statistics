# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# generate 1000 samples

data = np.random.normal(100, 10, 1000)
plt.hist(data)
plt.show()

Mean = np.mean(data)
std = np.std(data)

# sampling distribution of the sample means
means = []
for i in range(100):
    random.shuffle(data)
    samp_data = data[:100]
    means.append(np.mean(samp_data))
plt.hist(means)
plt.show()

# z-score test
z = (np.mean(means) - Mean) / (std /np.sqrt(100))
print(z)

# standardize the sample distribution of the sample means
for i in range(len(means)):
    means[i] = ((means[i] - Mean) / std)
plt.hist(means)
plt.show()

print(np.mean(means), np.std(means))
