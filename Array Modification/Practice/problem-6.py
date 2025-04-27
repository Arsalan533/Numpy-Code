import numpy as np

marks_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
new_marks_2d = np.insert(marks_2d, 1, [10, 11, 12], axis=0)

print(new_marks_2d)