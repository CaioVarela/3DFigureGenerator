import pandas as pd
from models import coneTrunk
from services.transformations import translationService
from services.transformations import scaleService

class ConeTrunkService:
    def connectTrunk(element1, element2, pc = [0, 0, 0], up = 0, down = 0):

        df1 = pd.DataFrame({"x": element1[0], "y":element1[1], "z":element1[2]})
        df2 = pd.DataFrame({"x": element2[0], "y":element2[1], "z":element2[2]})

        troX = []
        troY = []
        troZ = []  

        for i in range(len(df1)):
            troX.append(df1['x'][i])
            troY.append(df1['y'][i])
            troZ.append(df1['z'][i])

            if down:
                troX.append(pc[0])
                troY.append(pc[1])
                troZ.append(pc[2])

                troX.append(df1['x'][i])
                troY.append(df1['y'][i])
                troZ.append(df1['z'][i])

                

        for i in range(len(df1)):
            troX.append(df2['x'][i])
            troY.append(df2['y'][i])
            troZ.append(df2['z'][i])

            troX.append(df1['x'][i])
            troY.append(df1['y'][i])
            troZ.append(df1['z'][i])

            troX.append(df2['x'][i])
            troY.append(df2['y'][i])
            troZ.append(df2['z'][i])

            if up:
                troX.append(df2['x'][i])
                troY.append(df2['y'][i])
                troZ.append(df2['z'][i])
                
                troX.append(pc[0])
                troY.append(pc[1])
                troZ.append(pc[2])

                troX.append(df2['x'][i])
                troY.append(df2['y'][i])
                troZ.append(df2['z'][i])

    
        return troX, troY, troZ
    
    def add_coneTrunk(points, isCentralized=True, rb=2.5, rs=1.5, h=2, pc=[0, 0, 0], p=1/5):
        x, y, z = coneTrunk.ConeTrunk.coneTrunk(rb, rs, h, pc, p)

        if (isCentralized == False):
            points = translationService.TranslationService.translation(-10, -5, -5, [x, y, z])
            points = scaleService.ScaleService.scale(1/2, 1/2, 1/2, points)

            return points
        else: 
            return [x, y, z]