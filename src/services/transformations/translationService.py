import numpy as np

class TranslationService:
    def translation(x, y, z, pontos):
        one = np.ones(len(pontos[0]))
        pontos.append(one)
        result =  np.dot([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]], pontos)
        return result