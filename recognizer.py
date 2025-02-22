import numpy as np

class Recognizer:

    def __init__(self):
        try:
            self.matrix = np.load('matrix.npy')
        except FileNotFoundError:
            print("Ошибка: 'matrix.npy' не найден в системе!")
            self.matrix = None

    def reco(self):
        if self.matrix is None:
            return False

        rows = self.matrix.shape[0]
        coil = self.matrix.shape[1]

        # Проверка по строкам
        for r in range(rows):
            if coil <= 1:
                continue
            for c in range(1, coil):
                if self.matrix[r, c] != self.matrix[r, c - 1] - 1:
                    return False

        # Проверка по столбцам
        for c in range(coil):
            if rows <= 1:
                continue
            for r in range(1, rows):
                if self.matrix[r, c] != self.matrix[r - 1, c] + 1:
                    return False

        return True

#print(np.load('matrix.npy'))
#print("-" * 30)
recognizer_instance = Recognizer()
if recognizer_instance.matrix is not None:
    result = recognizer_instance.reco()
    print(result)
else:
    print("Ошибка: 'matrix.npy' не загружен.")