import numpy as np

rows = 8
cols = 8

matrix = np.zeros((rows, cols), dtype=int)

first_column = np.arange(5, 5 + rows)
matrix[:, 0] = first_column

for i in range(1, cols):
    matrix[:, i] = matrix[:, i-1] - 1

print(matrix)
print("-" * 30)

np.save('matrix.npy', matrix)
print("Матрица сохранена в matrix.npy")
