import numpy as np


class Matrix:
    def __init__(self, low, high, row, coil):
        self.name = 'matrix.npy'
        self.low = low
        self.high = high
        self.row = row
        self.coil = coil

    def create_matrix(self):
        matrix = np.random.randint(self.low, self.high, size=(self.row, self.coil))
        return matrix

    def save_matrix(self):
        np.save(self.name, self.create_matrix())

        print("Матрица сохранена в matrix.npy")

    def get_matrix(self):
        return np.load(self.name)

M = Matrix(1,9, 8,8)
M.save_matrix()
print("-" * 30)
print(M.get_matrix())
