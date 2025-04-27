import numpy as np

sales = np.array([[1000,2000,3000],
                [4000,5000,6000],
                [7000,8000,9000,]])

bonus =  np.array([100, 200, 300])

final_sales = sales + bonus  

print(final_sales)