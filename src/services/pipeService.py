import pandas as pd
from models import pipe
from services.transformations import translationService

class PipeService:
    def pipeConnect(h, circ, raio, pc):

        df = pd.DataFrame({"x": circ[0], "y":circ[1], "z":circ[2]})

        clX = []
        clY = []
        clZ = []  

        for i in range(len(df)):
            clX.append(df['x'][i])
            clY.append(df['y'][i])
            clZ.append(df['z'][i])

        for i in range(len(df)):
            clX.append(df['x'][i])
            clY.append(df['y'][i])
            clZ.append(df['z'][i] + h)

        for i in range(len(df)):
            clX.append(df['x'][i])
            clY.append(df['y'][i])
            clZ.append(df['z'][i] + h)

            clX.append(df['x'][i])
            clY.append(df['y'][i])
            clZ.append(df['z'][i])

            clX.append(df['x'][i])
            clY.append(df['y'][i])
            clZ.append(df['z'][i] + h)
    
        return clX, clY, clZ
    
    def add_pipe(points, isCentralized=True):
            x, y, z = pipe.Pipe.pipe(2, [0, 0, 0], p=1/5)
            
            if (isCentralized == False):
                points = translationService.TranslationService.translation(6, 4, 4, [x, y, z])
                return points
            else: 
                return [x, y, z]