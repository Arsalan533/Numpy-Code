import numpy as np

data = np.array([[10, 20, 30], [40, 50, 60]])

subjects_total = data.sum(axis=0)

print("Total marks in each subject:", subjects_total)