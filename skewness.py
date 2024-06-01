import pandas as pd

Data = pd.read_csv("Data.csv")

data = Data["data"]

print(data.head())