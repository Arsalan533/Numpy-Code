import numpy as np

scores = np.array([10,20,30,40,50])

normalized_scores = (scores - scores.min()) / (scores.max() - scores.min())

print(normalized_scores)