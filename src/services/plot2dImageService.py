import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

class Plot2dImageService:

    def plotImage_2d(points):
        dfs = []
        figs = []

        for i in points:
            df = pd.DataFrame({"x": i[0], "y":i[1]})
            dfs.append(df)
        
        for i in dfs:
            color = np.random.randint(255, size=3)
            fig = px.line(i, x="x", y="y", color_discrete_sequence=[f'rgb({color[0]}, {color[1]}, {color[2]})']) 
            figs.append(fig.data[0])

        fig = go.Figure(data=figs)
        
        fig.update_layout(width=800, height=600)  # Ajuste os valores conforme necessário

        # Ajustar os limites dos eixos
        novo_limite_x = [-10, 10]  # Substitua pelos valores desejados
        novo_limite_y = [-10, 10]  # Substitua pelos valores desejados

        fig.update_xaxes(range=novo_limite_x)
        fig.update_yaxes(range=novo_limite_y)


        fig.show()