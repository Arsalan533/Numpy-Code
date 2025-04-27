"""
np.insert(array, index, value, asix=None)
array -  Original array
index -
value -
axis - 
axis = 0,  row-wise
1 column wise


"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
new_arr = np.insert(arr, 1, 100, axis=0)
print(new_arr)