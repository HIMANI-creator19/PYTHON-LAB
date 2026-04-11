import numpy as np

q1 = np.array([
    [100, 150, 200],
    [120, 130,140],
    [90, 110, 160]
])

q2 = np.array([
    [110, 160, 210],
    [130, 140, 150],
    [100, 120,170]
])

print("Total Sales:\n",q1 + q2)
print("\nGrowth in Sales:\n",q2 -q1)
print("\nAverage Sales per Product:",np.mean(q2,axis=0))
print("\nRegion with highest sales:",np.argmax(np.sum(q2,axis=1) + 1))
print("\nTranspose of q2:\n",q2.T)