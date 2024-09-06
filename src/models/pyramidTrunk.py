import models.square as square
import services.trunkConnectService as trunkConnect
import numpy as np

class PyramidTrunk:
    def tronco(lb, ls, h, pc, p=1):

        x = []
        y = []
        z = []

        cont = 0

        while cont < h:
            quad1 = square.Square.quadrado((h*lb - cont*lb + cont*ls)/h, [pc[0], pc[1], pc[2] + cont])
            cont += p
            quad2 = square.Square.quadrado((h*lb - cont*lb + cont*ls)/h, [pc[0], pc[1], pc[2] + cont])

            if cont == p:
                tronco = trunkConnect.TrunkConnectService.ligarTronco(quad1, quad2, pc=pc, down=1)
                x += tronco[0]
                y += tronco[1]
                z += tronco[2]
                continue
            if cont == h:
                tronco = trunkConnect.TrunkConnectService.ligarTronco(quad1, quad2, pc=[pc[0], pc[1], pc[2] + h], up=1)
                x += tronco[0]
                y += tronco[1]
                z += tronco[2]
                continue

            tronco = trunkConnect.TrunkConnectService.ligarTronco(quad1, quad2)

            x += tronco[0]
            y += tronco[1]
            z += tronco[2]

            cont = np.round(cont, 2)
        
        return x, y, z