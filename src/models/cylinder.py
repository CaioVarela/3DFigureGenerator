import numpy as np
import services.circumferenceConnectService as circConnect
import models.circumference as circumference

class Cylinder:
    def cilindro(raio, pc, p=1):
        x = []
        y = []
        z = []

        h = 2*raio  
        cont = 0

        circ = circumference.Circumference.circunferencia(raio, pc)

        while cont <= h:
            cont = np.round(cont, 2)
            cil = circConnect.CircumferenceConnectService.ligarCirc(cont, circ, raio, pc)
            x += cil[0]
            y += cil[1]
            z += cil[2]
            
            cont += p
        
        return x, y, z