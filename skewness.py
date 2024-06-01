import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Mean(data):
    return np.mean(data)

def Median(data):
    return np.median(data)

def standard_deviation(data):
    return np.std(data)

Data = pd.read_csv("Data.csv")

data = Data["data"]

print(data.head())

u = Mean(data)
v = Median(data)
sigma = standard_deviation(data)

skewness = (u - v) / sigma

if skewness > 0 :
    print("positive skewness is ", skewness)
    
elif skewness < 0 :
    print("negative skewness is ", skewness)

else :
    print("skewness is zero")


plt.hist(data, color='blue')
plt.axvline(np.mean(data), color='red')
plt.legend()
plt.grid(True)
plt.show()