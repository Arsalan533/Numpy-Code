import numpy as np

sales = np.array([100, 200, 300, 400, 500])
new_sales = np.delete(sales, [1, 3])

print("Sales after delete", new_sales)