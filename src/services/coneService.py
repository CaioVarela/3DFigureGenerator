import pandas as pd
from models import cone
from services.transformations import translationService

class ConeService:
    def coneConnect(h, circ1, circ2, pc):

        df1 = pd.DataFrame({"x": circ1[0], "y":circ1[1], "z":circ1[2]})
        df2 = pd.DataFrame({"x": circ2[0], "y":circ2[1], "z":circ2[2]})

        cnX = []
        cnY = []
        cnZ = []  

        for i in range(len(df1)):
            cnX.append(df1['x'][i])
            cnY.append(df1['y'][i])
            cnZ.append(df1['z'][i])

            if h == 0:
                cnX.append(pc[0])
                cnY.append(pc[1])
                cnZ.append(pc[2])

                cnX.append(df1['x'][i])
                cnY.append(df1['y'][i])
                cnZ.append(df1['z'][i])

        for i in range(len(df1)):
            cnX.append(df2['x'][i])
            cnY.append(df2['y'][i])
            cnZ.append(df2['z'][i])

            cnX.append(df1['x'][i])
            cnY.append(df1['y'][i])
            cnZ.append(df1['z'][i])

            cnX.append(df2['x'][i])
            cnY.append(df2['y'][i])
            cnZ.append(df2['z'][i])
    
        return cnX, cnY, cnZ
    
    def add_cone(points, isCentralized=True):
        x, y, z = cone.Cone.cone(2, 3*2, [0, 0, 0])
        
        if (isCentralized == False):
            points = translationService.TranslationService.translation(2, 4, 0, [x, y, z])
            return points
        else: 
            return [x, y, z]