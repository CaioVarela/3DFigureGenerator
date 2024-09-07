import numpy as np
import services.pipeService as pipeService
import models.circumference as circumference

class Pipe:
    def pipe(raio, pc, p=1):
        x = []
        y = []
        z = []

        h = 2*raio  
        cont = 0

        circ = circumference.Circumference.circumference(raio, pc)

        while cont <= h:
            cont = np.round(cont, 2)
            cil = pipeService.PipeService.pipeConnect(cont, circ, raio, pc)
            x += cil[0]
            y += cil[1]
            z += cil[2]
            
            cont += p
        
        return x, y, z