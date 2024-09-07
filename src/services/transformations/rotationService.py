import numpy as np

class RotationService:
    def rotation_keeping_x(theta, pontos, tr = [0, 0, 0]):
        result = np.dot([[1, 0, 0, tr[0]], [0, 1, 0, tr[1]], [0, 0, 1, tr[2]], [0, 0, 0, 1]], [[1, 0, 0, 0], [0, np.cos(theta), -np.sin(theta), 0], [0, np.sin(theta), np.cos(theta), 0], [0, 0, 0, 1]])
        result = np.dot(result, [[1, 0, 0, -tr[0]], [0, 1, 0, -tr[1]], [0, 0, 1, -tr[2]], [0, 0, 0, 1]])
        result = np.dot(result, pontos)
        return result

    def rotation_keeping_y(theta, pontos, tr = [0, 0, 0]):
        result = np.dot([[1, 0, 0, tr[0]], [0, 1, 0, tr[1]], [0, 0, 1, tr[2]], [0, 0, 0, 1]], [[np.cos(theta), 0, -np.sin(theta), 0], [0, 1, 0, 0], [np.sin(theta), 0, np.cos(theta), 0], [0, 0, 0, 1]])
        result = np.dot(result, [[1, 0, 0, -tr[0]], [0, 1, 0, -tr[1]], [0, 0, 1, -tr[2]], [0, 0, 0, 1]])
        result = np.dot(result, pontos)
        return result

    def rotation_keeping_z(theta, pontos, tr = [0, 0, 0]):
        result = np.dot([[1, 0, 0, tr[0]], [0, 1, 0, tr[1]], [0, 0, 1, tr[2]], [0, 0, 0, 1]], [[np.cos(theta), -np.sin(theta), 0, 0], [np.sin(theta), np.cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        result = np.dot(result, [[1, 0, 0, -tr[0]], [0, 1, 0, -tr[1]], [0, 0, 1, -tr[2]], [0, 0, 0, 1]])
        result = np.dot(result, pontos)
        return result

    def toro_rotation(theta, x, y, z):
        ones = np.ones(len(x))
        pontos = list(zip(x, y, z, ones))
        pontos = np.transpose(pontos)
        result =  np.dot([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, -z[0]], [0, 0, 0, 1]], pontos) 
        result =  np.dot([[np.cos(theta), 0, -np.sin(theta), 0], [0, 1, 0, 0], [np.sin(theta), 0, np.cos(theta), 0], [0, 0, 0, 1]], result)
        result =  np.dot([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, z[0]], [0, 0, 0, 1]], result)
        xr, yr, zr, onesr = result
        return xr, yr, zr