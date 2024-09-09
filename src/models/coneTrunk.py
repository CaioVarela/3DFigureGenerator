import models.circumference as circumference
import services.coneTrunkService as coneTrunkService
import numpy as np

class ConeTrunk:
    def coneTrunk(rb, rs, h, pc, p=1):

        x = []
        y = []
        z = []

        cont = 0
        db = rb*2
        ds = rs*2

        while cont < h:
            quad1 = circumference.Circumference.circumference((h*db - cont*db + cont*ds)/h, [pc[0], pc[1], pc[2] + cont])
            cont += p
            quad2 = circumference.Circumference.circumference((h*db - cont*db + cont*ds)/h, [pc[0], pc[1], pc[2] + cont])

            if cont == p:
                tronco = coneTrunkService.ConeTrunkService.connectTrunk(quad1, quad2, pc=pc, down=1)
                x += tronco[0]
                y += tronco[1]
                z += tronco[2]
                continue
            if cont == h:
                tronco = coneTrunkService.ConeTrunkService.connectTrunk(quad1, quad2, pc=[pc[0], pc[1], pc[2] + h], up=1)
                x += tronco[0]
                y += tronco[1]
                z += tronco[2]
                continue

            tronco = coneTrunkService.ConeTrunkService.connectTrunk(quad1, quad2)

            x += tronco[0]
            y += tronco[1]
            z += tronco[2]

            cont = np.round(cont, 2)
        
        return x, y, z