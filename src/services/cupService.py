import pandas as pd
from models import cup
from services.transformations import translationService
import numpy as np

class CupService:
    def connectToroid(circ1, circ2):

        df1 = pd.DataFrame({"x": circ1[0], "y":circ1[1], "z":circ1[2]})
        df2 = pd.DataFrame({"x": circ2[0], "y":circ2[1], "z":circ2[2]})

        esfX = []
        esfY = []
        esfZ = []  

        for i in range(len(df1)):
            esfX.append(df1['x'][i])
            esfY.append(df1['y'][i])
            esfZ.append(df1['z'][i])

        for i in range(len(df1)):
            esfX.append(df2['x'][i])
            esfY.append(df2['y'][i])
            esfZ.append(df2['z'][i])

            esfX.append(df1['x'][i])
            esfY.append(df1['y'][i])
            esfZ.append(df1['z'][i])

            esfX.append(df2['x'][i])
            esfY.append(df2['y'][i])
            esfZ.append(df2['z'][i])
    
        return esfX, esfY, esfZ
    
    def add_cup(points, isCentralized=True):
            x, y, z = cup.Cup.cup(0.5, np.pi/36, [1, 0, 0], [-4, 1, 4])
            
            if (isCentralized == False):
                points = translationService.TranslationService.translation(-5, -5, -3, [x, y, z])
                return points
            else: 
                return [x, y, z]