import models.square as square
import services.coneTrunkService as coneTrunkService
import services.boxService as boxService
import numpy as np

class Box:
    def box(l, h, pc, p=1):

        x = []
        y = []
        z = []

        cont = 0

        while cont < h:
            
            quad1 = square.Square.square(l, [pc[0], pc[1], pc[2] + cont])
            cont += p
            quad2 = square.Square.square(l, [pc[0], pc[1], pc[2] + cont])

            if cont == p:
                tronco = coneTrunkService.ConeTrunkService.connectTrunk(quad1, quad2, pc=pc, down=1)
                x += tronco[0]
                y += tronco[1]
                z += tronco[2]
                continue

            tronco = boxService.BoxService.boxConnect(quad1, quad2)

            x += tronco[0]
            y += tronco[1]
            z += tronco[2]

            cont = np.round(cont, 2)
        
        return x, y, z