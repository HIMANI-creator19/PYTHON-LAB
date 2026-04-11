import numpy as np

sales = np.array([
    [100, 120, 130, 140],
    [90, 110, 115, 120],
    [150, 160,170,180]
])

print("Total sales per store :",np.sum(sales,axis=1))
print("Overall Average : ",np.mean(sales))