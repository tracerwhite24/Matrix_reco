import numpy as np

matrix = np.load('matrix.npy')

def reco():

    rows = matrix.shape[0]
    cols = matrix.shape[1]

    # Проверка по строкам
    for r in range(rows):
        if cols <= 1:
            continue
        for c in range(1, cols):
            if matrix[r, c] != matrix[r, c - 1] - 1:
                return False

    # Проверка по столбцам
    for c in range(cols):
        if rows <= 1:
            continue
        for r in range(1, rows):
            if matrix[r, c] != matrix[r - 1, c] + 1:
                return False

    return True

print(matrix)
print("-" * 30)
print(reco())
