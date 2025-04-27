import numpy as np

img = np.array([[0, 255 ,0], [255, 0, 255], [0, 255, 0]])
flattened_img = img.flatten()

print("Flattened Image Array", flattened_img)
