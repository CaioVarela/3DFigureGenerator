import tkinter as tk
from services.plot3dImageService import Plot3dImageService
from services.boxService import BoxService
from services.coneService import ConeService
from services.pipeService import PipeService
from services.coneTrunkService import ConeTrunkService

class InterfaceMany3DFigures:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface 3D com Diversas Figuras")

        # Botão para gerar a imagem
        self.plot_button = tk.Button(root, text="Gerar Imagem", command=self.select_object)
        self.plot_button.pack()

    def select_object(self):
        self.points = []

        self.points.append(BoxService.add_box(self.points))
        self.points.append(ConeService.add_cone(self.points))
        self.points.append(PipeService.add_pipe(self.points))
        # TODO: Após criar service do teu caneco, adiciona aqui
        # self.points.append(CupService.add_cup(self.points))
        self.points.append(ConeTrunkService.add_coneTrunk(self.points))

        self.plot_points()

        self.points = []

        self.points.append(BoxService.add_box(self.points, False))
        self.points.append(ConeService.add_cone(self.points, False))
        self.points.append(PipeService.add_pipe(self.points, False))
        # TODO: Após criar service do teu caneco, adiciona aqui
        # self.points.append(CupService.add_cup(self.points, False))
        self.points.append(ConeTrunkService.add_coneTrunk(self.points, False))

        self.plot_points()


    def plot_points(self):
        if self.points:
            Plot3dImageService.plot_image(self.points)
        else:
            print("Nenhum ponto foi adicionado.")
