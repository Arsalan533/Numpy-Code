import numpy as np

price_per_item = np.array([10, 20, 30])

sales = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

total_sales = sales * price_per_item

print(total_sales)