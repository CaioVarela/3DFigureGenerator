import models.circumference as circumference
import models.pipe as pipe
from services.transformations import scaleService
import services.transformations.rotationService as rotateService
import services.transformations.translationService as translateService
import services.cupService as cupService
import numpy as np

class Cup:
    def cup(cupR, cupH, toroR, pc, pc_toro):
        x = []
        y = []
        z = []

        ang = np.pi/36

        var = 0

        xc, yc, zc = circumference.Circumference.circumference(toroR, pc)

        while var < 2*np.pi/2:

            x1, y1, z1 = rotateService.RotationService.toro_rotation(var, xc, yc, zc)
            x1, y1, z1, _ = translateService.TranslationService.translation(pc_toro[0], pc_toro[1]-pc[1], pc_toro[2]-pc[2], [x1, y1, z1])
            var += ang
            x2, y2, z2 = rotateService.RotationService.toro_rotation(var, xc, yc, zc)
            x2, y2, z2, _ = translateService.TranslationService.translation(pc_toro[0], pc_toro[1]-pc[1], pc_toro[2]-pc[2], [x2, y2, z2])


            toro = cupService.CupService.connectToroid([x1, y1, z1], [x2, y2, z2])
            x += toro[0]
            y += toro[1]
            z += toro[2]

        x, y, z = rotateService.RotationService.toro_rotation(190, x, y, z)

        x1, y1, z1 = pipe.Pipe.pipe(cupR, cupH, [1.2, 1, -1.5], p=1/5, hasBottom=True)
        x1, y1, z1 = np.array(x1), np.array(y1), np.array(z1)
        pontos_pipe = np.vstack([x1, y1, z1, np.ones(len(x1))])
        x1, y1, z1, _ = scaleService.ScaleService.scale(1, 1, 1.3, pontos_pipe)

        xPoints = np.concatenate((x, x1))
        yPoints = np.concatenate((y, y1))
        zPoints = np.concatenate((z, z1))

        points = xPoints, yPoints, zPoints

        return points
    