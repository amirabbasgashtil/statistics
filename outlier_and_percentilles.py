import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Data.csv')

data = data['data']

# percentilles for average
counter = 0
avg = np.average(data)

for d in data:
    if d < avg:
        counter += 1

print(counter, '% percentilles below the average.')

'''
   we can see outliers data in this boxplot 
'''

sns.boxplot(data)
plt.show()