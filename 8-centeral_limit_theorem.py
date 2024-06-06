# with any distribution we start => sample Means would be normally distributed
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
import random

Data = read_csv("Data.csv")

data = Data["data"]

copy_data = np.copy(data)

plt.hist(copy_data)
plt.show()

sample_Means=[]

# taking 30 samples and add its means to sample_means list
for i in range(30):
    random.shuffle(copy_data)
    sample = copy_data[:30]
    sample_Means.append(np.mean(sample))

plt.hist(sample_Means)
plt.xlabel('Means')
plt.ylabel('Repetitions')
plt.show()
