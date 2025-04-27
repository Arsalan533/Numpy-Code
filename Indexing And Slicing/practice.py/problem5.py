import numpy as np

# marks = np.random.randint(10, 40, (5, 3))
# print("All Makks :\n", marks)

# good_students = marks[marks[:, 1]  > 20]
# print("Students with >20 in Subjects 2:\n", good_students)

marks = np.random.randint(10, 40, (5, 3))
print("All Marks :\n", marks)

good_students = marks[marks[:, 1] > 20]
print("Students with >20 in subjects 2:\n", good_students)