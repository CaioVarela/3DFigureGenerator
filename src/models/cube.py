import models.square as square
import services.trunkConnectService as trunkConnect
import services.cubeConnectService as cubeConnect
import numpy as np

class Cube:
    def cubo(l, pc, p=1):

        x = []
        y = []
        z = []

        cont = 0
        h = l

        while cont < h:
            
            quad1 = square.Square.quadrado(l, [pc[0], pc[1], pc[2] + cont])
            cont += p
            quad2 = square.Square.quadrado(l, [pc[0], pc[1], pc[2] + cont])

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

            tronco = cubeConnect.CubeConnectService.ligarCubo(quad1, quad2)

            x += tronco[0]
            y += tronco[1]
            z += tronco[2]

            cont = np.round(cont, 2)
        
        return x, y, z