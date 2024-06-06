# ANOVA         ANalysis Of VAriance

import pandas as pd
import numpy as np
import random
from scipy.stats import f_oneway

data = pd.read_csv('Data.csv')

data_lst_copy = list(data['data'])
random.shuffle(data_lst_copy)
group1 = data_lst_copy[:14]
group2 = data_lst_copy[14:28]
group3 = data_lst_copy[28:]

'''
print(group1)
print(group2)
print(group3)
'''
print(f_oneway(group1, group2, group3))