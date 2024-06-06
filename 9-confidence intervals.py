import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Data.csv")
data = data["data"]

sample_mean = []
for i in range(1000):
    random.shuffle(data)
    sample = data[:30]
    sample_mean.append(np.mean(sample))

plt.style.use('_mpl-gallery')
x = sample_mean
y = [4] * 1000
fig, ax = plt.subplots()
ax.stem(x, y)
ax.set(xlim=(20, 50), xticks=np.arange(1, 50),
       ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()

confidence_level = 0.95
confid_int_UpperBound = np.mean(sample_mean) + confidence_level * (np.std(sample_mean) / np.sqrt(1000))
confid_int_LowerBound = np.mean(sample_mean) - confidence_level * (np.std(sample_mean) / np.sqrt(1000))

# now we have a interval that have 95 percent of means in it
confid_int = np.array([confid_int_LowerBound, confid_int_UpperBound])
print(confid_int)
