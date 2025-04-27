"""
Reshape(Rows, columns) specify new shape 
if dimensions match

"""

import numpy as np

arr =  np.array([1,2,3,4,5,6])
reshaped_Arr = arr.reshape(2, 3)
print(reshaped_Arr)