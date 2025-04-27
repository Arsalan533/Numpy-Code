import numpy as np

sales = np.array([100, 200, 300, 400, 500, 600, 700,])
new_sales = np.split(sales, [2, 5])

print(new_sales)