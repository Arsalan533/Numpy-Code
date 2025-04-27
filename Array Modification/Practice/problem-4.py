import numpy as np

sales_2d = np.array([[100,200,300], [400,500,600], [700,800,900]])
new_sales_2d = np.delete(sales_2d, [0, 1], axis=1)

print(new_sales_2d)   