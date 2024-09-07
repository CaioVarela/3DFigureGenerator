import tkinter as tk
from tkinter import ttk
from services.plot3dImageService import Plot3dImageService
from services.boxService import BoxService
from services.coneService import ConeService
from services.pipeService import PipeService
from services.coneTrunkService import ConeTrunkService
from services.cupService import CupService

class Interface3D:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface 3D")
        
        self.figures = ["Caixa", "Cone", "Tronco de Cone", "Cano", "Caneca"]  # Lista de figuras disponíveis (pode adicionar mais)
        
        # Label de instruções
        self.label = tk.Label(root, text="Escolha uma figura 3D:")
        self.label.pack()

        # Combobox para selecionar a figura 3D
        self.figure_selector = ttk.Combobox(root, values=self.figures)
        self.figure_selector.pack()

        # Botão para gerar a imagem
        self.plot_button = tk.Button(root, text="Gerar Imagem", command=self.select_object)
        self.plot_button.pack()

    def select_object(self):
        figure = self.figure_selector.get()
        self.points = []

        if figure == "Caixa":
            self.points.append(BoxService.add_box(self.points))
        if figure == "Cone":
            self.points.append(ConeService.add_cone(self.points))
        if figure == "Cano":
            self.points.append(PipeService.add_pipe(self.points))
        if figure == "Caneca":
            self.points.append(CupService.add_cup(self.points))
        if figure == "Tronco de Cone":
            self.points.append(ConeTrunkService.add_coneTrunk(self.points))

        self.plot_points()


    def plot_points(self):
        if self.points:
            Plot3dImageService.plot_image(self.points)
        else:
            print("Nenhum ponto foi adicionado.")
