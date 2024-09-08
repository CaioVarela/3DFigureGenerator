import tkinter as tk
from services.boxService import BoxService
from services.camService import CamService
import numpy as np

from services.coneService import ConeService
from services.coneTrunkService import ConeTrunkService
from services.cupService import CupService
from services.pipeService import PipeService
from services.plot3dImageService import Plot3dImageService

class InterfaceMany3DFiguresByCam:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface 3D com Diversas Figuras no Sistema de Coordenadas da Câmera")

        # Botão para gerar a imagem
        self.plot_button = tk.Button(root, text="Gerar Imagem", command=self.generate_image)
        self.plot_button.pack()

    def generate_image(self):
        box = BoxService.add_box([], False)
        cone = ConeService.add_cone([], False)
        pipe = PipeService.add_pipe([], False)
        cup = CupService.add_cup([], False)
        coneTrunk = ConeTrunkService.add_coneTrunk([], False)
        V = CamService.get_coordinate_system()
        
        box_ = np.dot(V, box)
        cone_ = np.dot(V, cone)
        pipe_ = np.dot(V, pipe)
        cup_ = np.dot(V, cup)
        coneTrunk_ = np.dot(V, coneTrunk)
        mundo = np.dot(V, [[0], [0], [0], [1]])

        return Plot3dImageService.plot_image([box_, cone_, pipe_, cup_, coneTrunk_], mundo)