import numpy as np

class ScaleService:
    def scale(x, y, z, pontos):
        scale_matrix = np.array([
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ])

        result = np.dot(scale_matrix, pontos)
        return result