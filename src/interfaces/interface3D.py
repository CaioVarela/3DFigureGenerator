import tkinter as tk
from tkinter import ttk
from services.plot3dImageService import Plot3dImageService
from models import cube, pyramidTrunk, cone, cylinder

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
            self.add_box()
        if figure == "Cone":
            self.add_cone()
        if figure == "Cano":
            self.add_pipe()
        if figure == "Caneca":
            self.add_cup()
        if figure == "Tronco de Cone":
            self.add_coneTrunk()

        self.plot_points()

    def add_box(self):
        x, y, z = cube.Cube.cubo(2, [0, 0, 0])
        self.points.append([x, y, z])

    def add_cone(self):
        x, y, z = cone.Cone.cone(2, 3*2, [0, 0, 0])
        self.points.append([x, y, z])

    def add_pipe(self):
        x, y, z = cylinder.Cylinder.cilindro(2, [0, 0, 0], p=1/5)
        self.points.append([x, y, z])
    
    def add_cup(self):
        print("mb de chapeuzim")
        
    def add_coneTrunk(self):
        x, y, z = pyramidTrunk.PyramidTrunk.tronco(5, 3, 2, [0, 0, 0], 1/5)
        self.points.append([x, y, z])


    def plot_points(self):
        if self.points:
            Plot3dImageService.plot_image(self.points)
        else:
            print("Nenhum ponto foi adicionado.")
