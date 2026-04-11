import numpy as np

marks = np.array([[80, 85, 90],[70, 75, 80],[90, 88, 95]])
print("Marks Table :\n",marks)

sub_avg = np.mean(marks,axis=0) # axis=0 means column wise operation and axis=1 means row wise operation
print("Average marks per student :",sub_avg)

sub_avg1 = np.mean(marks,axis=1)
print("Average marks per subject :",sub_avg1)

print(marks.ndim)
print(marks.shape)
print(marks.size)