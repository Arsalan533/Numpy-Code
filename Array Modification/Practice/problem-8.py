import numpy as np

store1 = np.array([10,20,30])
store2 = np.array([40,50,60])
store3 = np.array([70,80,90])

vertically_stacked = np.vstack((store1, store2, store3))
print(vertically_stacked)

horizontal_stacked = np.hstack((store1, store2, store3))
print(horizontal_stacked)

