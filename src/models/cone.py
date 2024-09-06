import services.coneConnectService as coneConnect
import models.circumference as circ

class Cone:
    def cone(raio, pc, p=1):
        x = []
        y = []
        z = []

        h = 3*raio  
        cont = 0

        while cont < h:

            circ1 = circ.Circumference.circunferencia(raio, [pc[0], pc[1], pc[2] + cont])
            circ2 = circ.Circumference.circunferencia((3*raio - p)/3, [pc[0], pc[1], pc[2] + cont+p])

            cone = coneConnect.ConeConnectService.ligarCone(cont, circ1, circ2, pc)
            x += cone[0]
            y += cone[1]
            z += cone[2]
            
            raio = (3*raio - p)/3
            cont += p
        
        return x, y, z