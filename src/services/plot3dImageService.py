import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

class Plot3dImageService:
    
    def plot_image(points, mundo=[[0], [0], [0], [1]]):
        dfs = []
        figs = []

        for i in points:
            df = pd.DataFrame({"x": i[0], "y": i[1], "z": i[2]})
            dfs.append(df)

        for i in dfs:
            color = np.random.randint(255, size=3)
            fig = px.line_3d(i, x="x", y="y", z="z", color_discrete_sequence=[f'rgb({color[0]}, {color[1]}, {color[2]})'])
            figs.append(fig.data[0])

        fig = go.Figure(data=figs)

        lines = [
            {'x': [0, 0], 'y': [0, 0], 'z': [-10, 10]},
            {'x': [0, 0], 'y': [-10, 10], 'z': [0, 0]},
            {'x': [-10, 10], 'y': [0, 0], 'z': [0, 0]}
        ]

        for line in lines:
            fig.add_scatter3d(mode='lines', x=line['x'], y=line['y'], z=line['z'], line=dict(color='black'))

        new_point = {'x': mundo[0], 'y': mundo[1], 'z': mundo[2]}
        df_mundo = pd.DataFrame(new_point)
        fig.add_trace(px.scatter_3d(df_mundo, x='x', y='y', z='z', size=[0.5]).data[0])

        fig.update_layout(
            scene=dict(
                xaxis=dict(range=[-10, 10]),
                yaxis=dict(range=[-10, 10]),
                zaxis=dict(range=[-10, 10]),
                aspectmode="cube",
            )
        )

        fig.show()