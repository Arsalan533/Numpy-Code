import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(3, -1)


print("Auto-reshaped array:")
print(reshaped)