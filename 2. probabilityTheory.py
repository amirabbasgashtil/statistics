# if randomly pick a number in data chance of grtting 21 would be :
import pandas as pd

data = pd.read_csv("Data.csv")
data = data['data']

count = 0
for d in data:
    if d == 21:
        count+=1


chance = (count / data.size ) * 100

print('chance of getting 21 is ', round(chance, 2),'%')