# Cumulative distribution function
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Data.csv")
data = data['data']

last_distribution = 0
lngth = data.size

def cumulative_distribution(item):
    count = 0
    for i in range(data.size):
        if data[i] <= item:
            count +=1
    cdf = (count / lngth)
    return cdf

lst = []
for d in data:
    lst.append((d, cumulative_distribution(d)))

for element in lst:
    print(element)

lst_x = [item[0] for item in lst]
lst_y = [item[1] for item in lst]
plt.plot(lst_x, lst_y)
plt.show()