import pandas as pd

class CircumferenceConnectService:
    def ligarCirc(h, circ, raio, pc):

        df = pd.DataFrame({"x": circ[0], "y":circ[1], "z":circ[2]})

        clX = []
        clY = []
        clZ = []  

        for i in range(len(df)):
            clX.append(df['x'][i])
            clY.append(df['y'][i])
            clZ.append(df['z'][i])

            if h == 0:
                clX.append(pc[0])
                clY.append(pc[1])
                clZ.append(pc[2])

                clX.append(df['x'][i])
                clY.append(df['y'][i])
                clZ.append(df['z'][i])

        for i in range(len(df)):
            clX.append(df['x'][i])
            clY.append(df['y'][i])
            clZ.append(df['z'][i] + h)
            if h == 2*raio:
                clX.append(pc[0])
                clY.append(pc[1])
                clZ.append(pc[2] + h)

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