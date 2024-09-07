import services.coneService as coneService
import models.circumference as circ

class Cone:
    def cone(raio, h, pc, p=1):
        x = []
        y = []
        z = []

        cont = 0

        while cont < h:

            circ1 = circ.Circumference.circumference(raio, [pc[0], pc[1], pc[2] + cont])
            circ2 = circ.Circumference.circumference((3*raio - p)/3, [pc[0], pc[1], pc[2] + cont+p])

            cone = coneService.ConeService.coneConnect(cont, circ1, circ2, pc)
            x += cone[0]
            y += cone[1]
            z += cone[2]
            
            raio = (3*raio - p)/3
            cont += p
        
        return x, y, z