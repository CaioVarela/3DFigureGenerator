import numpy as np
import models.circumference as circ
import services.sphereConnectService as sphereConnect

class Sphere:
    def esfera(raio, pc, p = 1/2):

        x = []
        y = []
        z = []
        
        cont = 0 

        while cont < raio:
            
            circ1 = circ.Circumference.circumference(np.sqrt([2*cont*raio - cont*cont])[0], [pc[0], pc[1], pc[2] - raio + cont])
            cont += p
            circ2 = circ.Circumference.circumference(np.sqrt([2*cont*raio - cont*cont])[0], [pc[0], pc[1], pc[2] - raio + cont])

            esfera = sphereConnect.SphereConnectService.connectSphere(circ1, circ2)
            x += esfera[0]
            y += esfera[1]
            z += esfera[2]

            cont = np.round(cont, 2)
        
        cont = 0

        while cont < raio:
            
            circ1 = circ.Circumference.circumference(np.sqrt([raio*raio - cont*cont])[0], [pc[0], pc[1], pc[2] + cont])
            cont += p
            circ2 = circ.Circumference.circumference(np.sqrt([raio*raio - cont*cont])[0], [pc[0], pc[1], pc[2] + cont])

            esfera = sphereConnect.SphereConnectService.connectSphere(circ1, circ2)
            x += esfera[0]
            y += esfera[1]
            z += esfera[2]

            cont = np.round(cont, 2)
            
        return x, y, z