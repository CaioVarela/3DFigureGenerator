import pandas as pd
from models import box
from services.transformations import translationService

class BoxService:
    def boxConnect(quad1, quad2, pc = [0, 0, 0], up = 0, down = 0):
        df1 = pd.DataFrame({"x": quad1[0], "y":quad1[1], "z":quad1[2]})
        df2 = pd.DataFrame({"x": quad2[0], "y":quad2[1], "z":quad2[2]})

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
    
    def add_box(points, isCentralized=True):
        x, y, z = box.Box.box(2, [0, 0, 0], 1/5)

        if (isCentralized == False):
            points = translationService.TranslationService.translation(5, -5, 5, [x, y, z])
            return points

        return [x, y, z]