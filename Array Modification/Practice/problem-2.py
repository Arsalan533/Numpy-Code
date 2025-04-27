import numpy as np

class1 = np.array([10,20,30,])
class2 = np.array([40,50,60,])
class3 = np.array([70,80,90,])

combined =  np.concatenate([class1, class2, class3])
print("Print concatenated class marks:", combined)
