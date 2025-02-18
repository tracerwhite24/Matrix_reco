import numpy as np

rows = 8
cols = 8

low = 1
high = 9
matrix = np.random.randint(low, high, size=(rows, cols))

print(f"Матрица, заполненная случайными целыми числами от {low} до {high-1}:")
print(matrix)
print("-" * 30)

np.save('matrix.npy', matrix)
print("Матрица сохранена в matrix.npy")
