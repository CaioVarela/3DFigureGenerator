import models.circumference as circumference
import services.rotationService as rotateService
import services.translationService as translateService
import services.toroidConnectService as toroidConnect
import numpy as np

class Toroid:
    def toroide(raio, ang, pc, pc_toro):
        x = []
        y = []
        z = []

        var = 0

        xc, yc, zc = circumference.Circumference.circunferencia(raio, pc)

        while var < 2*np.pi:

            x1, y1, z1 = rotateService.RotationService.rotacao_toro(var, xc, yc, zc)
            ones = np.ones(len(x1))
            x1, y1, z1, ones = translateService.TranslationService.translacao(pc_toro[0], pc_toro[1]-pc[1], pc_toro[2]-pc[2], [x1, y1, z1])
            var += ang
            x2, y2, z2 = rotateService.RotationService.rotacao_toro(var, xc, yc, zc)
            x2, y2, z2, ones = translateService.TranslationService.translacao(pc_toro[0], pc_toro[1]-pc[1], pc_toro[2]-pc[2], [x2, y2, z2])

        
            toro = toroidConnect.ToroidConnectService.ligarToroide([x1, y1, z1], [x2, y2, z2])
            x += toro[0] 
            y += toro[1]
            z += toro[2]

        return x, y, z