import numpy as np

class ScaleService:
    def scale(x, y, z, pontos):
        result = np.dot([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, 0, z], [0, 0, 0, 1]], pontos)
        return result