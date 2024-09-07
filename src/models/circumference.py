import services.transformations.rotationService as rotate
import numpy as np

class Circumference:
    def circumference(raio, pc, num_points=100):
        # Definindo os pontos principais (0°, 90°, 180°, 270°)
        p0 = np.array([pc[0] + raio, pc[1], pc[2]])  # 0°
        p1 = np.array([pc[0], pc[1] + raio, pc[2]])  # 90°
        p2 = np.array([pc[0] - raio, pc[1], pc[2]])  # 180°
        p3 = np.array([pc[0], pc[1] - raio, pc[2]])  # 270°

        # Vetores tangentes para suavizar as transições entre os pontos
        t0 = np.array([0, raio * np.pi / 2, 0])   # Tangente inicial para p0
        t1 = np.array([-raio * np.pi / 2, 0, 0])  # Tangente para p1
        t2 = np.array([0, -raio * np.pi / 2, 0])  # Tangente para p2
        t3 = np.array([raio * np.pi / 2, 0, 0])   # Tangente para p3

        # Dividir os pontos uniformemente entre as quatro curvas
        num_points_per_curve = num_points // 4

        # Criar as quatro curvas de Hermite
        curve1 = Circumference.hermite_curve(p0, p1, t0, t1, num_points_per_curve)
        curve2 = Circumference.hermite_curve(p1, p2, t1, t2, num_points_per_curve)
        curve3 = Circumference.hermite_curve(p2, p3, t2, t3, num_points_per_curve)
        curve4 = Circumference.hermite_curve(p3, p0, t3, t0, num_points_per_curve)

        # Combinar as quatro curvas em uma única lista de pontos
        curve = np.concatenate([curve1, curve2, curve3, curve4])

        # Separar as coordenadas x, y, z da curva resultante
        x = curve[:, 0].tolist()
        y = curve[:, 1].tolist()
        z = curve[:, 2].tolist()

        return x, y, z

    def hermite_curve(p0, p1, t0, t1, num_points=100):
        t = np.linspace(0, 1, num_points)
        h00 = 2 * t**3 - 3 * t**2 + 1
        h01 = -2 * t**3 + 3 * t**2
        h10 = t**3 - 2 * t**2 + t
        h11 = t**3 - t**2
    
        curve = (h00[:, np.newaxis] * p0 +
                 h01[:, np.newaxis] * p1 +
                 h10[:, np.newaxis] * t0 +
                 h11[:, np.newaxis] * t1)
        return curve