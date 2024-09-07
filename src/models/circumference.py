import services.transformations.rotationService as rotate
import numpy as np

class Circumference:
    def circumference(raio, pc, grau=np.pi/12):
        x, y, z = [], [], []
        ang = grau
        start = [pc[0] + raio, pc[1], pc[2], 1]
        x.append(start[0]), y.append(start[1]), z.append(start[2])

        while ang <= 2*np.pi:
            prox = rotate.RotationService.rotation_keeping_z(ang, start, pc)
            x.append(prox[0]), y.append(prox[1]), z.append(prox[2])
            ang += grau

        x.append(start[0]), y.append(start[1]), z.append(start[2])
        return x, y, z