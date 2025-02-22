import numpy as np

class Matrix:
    def __init__(self, low, high, row, coil):
        self.name = 'matrix.npy'
        self.low = low
        self.high = high
        self.row = row
        self.coil = coil

    def create_matrix(self):
        matrix = np.zeros((self.row, self.coil), dtype=int)
        return matrix

    def fill_matrix(self):
        matrix = self.create_matrix()
        first_column = np.arange(5, 5 + self.row)
        matrix[:, 0] = first_column
        for i in range(1, self.coil):
            matrix[:, i] = matrix[:, i - 1] - 1
        return matrix

    def save_matrix(self):
        matrix_to_save = self.fill_matrix()
        np.save(self.name, matrix_to_save)
        print("Матрица сохранена в matrix.npy")

    def get_matrix(self):
        return np.load(self.name)

M = Matrix(1,9, 8,8)
M.save_matrix()
print("-" * 30)
print(M.get_matrix())
