import numpy as np
from services.boxService import BoxService
from services.coneService import ConeService
from services.pipeService import PipeService
from services.coneTrunkService import ConeTrunkService
from services.cupService import CupService

class CamService:    
    def pontoMedio(figures):
        mean = []

        for figure in figures:

            arr = []

            points_t = np.transpose(figure)
            points_t = np.unique(points_t, axis=0)

            for point in points_t:
                arr.append(point)

            x = np.sum(arr, axis=0)
            x = np.round(x / len(arr), 2)
            mean.append(x)

        return mean

    def get_coordinate_system():
        points = []
        box = BoxService.add_box(points, False)
        cone = ConeService.add_cone(points, False)
        pipe = PipeService.add_pipe(points, False)
        cup = CupService.add_cup(points, False)
        coneTrunk = ConeTrunkService.add_coneTrunk(points, False)

        points.append(box)
        points.append(cone)
        points.append(pipe)
        points.append(cup)
        points.append(coneTrunk)

        c = np.array([1, 1, -1])
        pm = np.mean(CamService.pontoMedio(points), axis=0)
        pm = list(pm)
        del(pm[3])
        pm = np.array(pm)

        n = pm - c
        norm = np.linalg.norm(n)
        n = n/norm  

        aux = np.array([1, 0, 0])

        v = aux - (np.sum(aux*n)/np.sum(n*n))*n
        norm = np.linalg.norm(v)
        v = v/norm

        u = np.cross(v, n)

        V = [[u[0], u[1], u[2], -c[0]*u[0]-c[1]*u[1]-c[2]*u[2]],
             [v[0], v[1], v[2], -c[0]*v[0]-c[1]*v[1]-c[2]*v[2]],
             [n[0], n[1], n[2], -c[0]*n[0]-c[1]*n[1]-c[2]*n[2]],
             [0, 0, 0, 1]]
        
        return V