import numpy as np

prices = np.array([3, 1, 2, 4, 5, 9, 12, 8, 7])
expensive_items = prices[prices > 5]
print("Products over $5:\n", expensive_items)