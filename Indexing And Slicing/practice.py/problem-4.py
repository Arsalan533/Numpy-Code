import numpy as np

# attendance = np.zeros((3, 3), dtype=int)
# print("Before Update:\n", attendance)

# attendance[:, -1] = 1
# print("After Update:\n", attendance)

attendance  = np.zeros((3, 3), dtype=int)
print("Before Update: \n", attendance)

attendance[:, -1] = 1
print("After Update:\n", attendance)