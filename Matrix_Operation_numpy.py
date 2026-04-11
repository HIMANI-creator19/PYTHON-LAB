import numpy as np

Matrix_A = np.array([
    [50,60,80],
    [56,90,40],
    [80,90,85]
])

Matrix_B = np.array([
    [78,98,76],
    [89,90,90],
    [69,90,90]
])

addition = Matrix_A + Matrix_B
print("Addition(Total Marks):",addition)

sub = Matrix_B - Matrix_A
print("\nSubtraction(Improvement):\n",sub)

elementwise = Matrix_A * Matrix_B
print("\nElement wise Multiplication:\n",elementwise)

matrix_mult = np.dot(Matrix_A, Matrix_B)
print("\nMatrix Multiplication:\n",matrix_mult)

transpose_a = Matrix_A.T
print("\nTranspose of Matrix_A:\n",transpose_a)

