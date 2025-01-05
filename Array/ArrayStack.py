
import numpy as np
import sys
import pandas as pd


# How do I print the full NumPy array, without truncation?

np.set_printoptions(threshold=sys.maxsize)

# print(np.arange(10000).reshape(250,40))
# ---------------------------------------------------------------


# Dump a NumPy array into a csv file

a = np.array([[1,2,3],[4,5,6],[2,7,8]])

# np.savetxt('save.csv',a,delimiter= ', ',fmt='%d')

# for string use fmt = '%s'
# ---------------------------------------------------------------


# Convert Pandas dataframe to NumPy array

df = pd.DataFrame(data = {'A':[1,2,3], 'B':[3,4,5], 'C':[6,7,8]}, index= ['a','b','c'])
print(df.to_numpy())