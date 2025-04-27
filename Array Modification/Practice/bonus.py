import numpy as np

sales_data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

#  1. Delete the row
modified_data = np.delete(sales_data, -1, axis=0)


# 2. Insert a new row
modified_data = np.insert(modified_data, 1, [1, 4, 9], axis=0)

# 3. Stack the modified data with another array
new_data = np.array([[200, 210, 220], [230, 240, 250]])
final_data = np.vstack([modified_data, new_data])

print(final_data)