import tkinter as tk
from tkinter import ttk, simpledialog
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

        # Botão para adicionar valores
        self.plot_button = tk.Button(root, text="Adicione os Valores", command=self.select_object)
        self.plot_button.pack()

        # Botão para gerar a imagem
        self.plot_button = tk.Button(root, text="Gerar Imagem", command=self.plot_points)
        self.plot_button.pack()

    def select_object(self):
        figure = self.figure_selector.get()
        self.points = []

        if figure == "Caixa":
            l = simpledialog.askfloat("Input", "Insira o lado da caixa:")
            h = simpledialog.askfloat("Input", "Insira a altura da caixa:")
            self.points.append(BoxService.add_box(self.points, True, l, h))
        if figure == "Cone":
            r = simpledialog.askfloat("Input", "Insira o raio do cone:")
            h = simpledialog.askfloat("Input", "Insira a altura do cone:")
            self.points.append(ConeService.add_cone(self.points, True, r, h))
        if figure == "Cano":
            r = simpledialog.askfloat("Input", "Insira o raio do cone:")
            h = simpledialog.askfloat("Input", "Insira a altura do cone:")
            self.points.append(PipeService.add_pipe(self.points, True, r, h))
        if figure == "Caneca":
            cupR = simpledialog.askfloat("Input", "Insira o raio da base da caneca:")
            cupH = simpledialog.askfloat("Input", "Insira a altura da caneca:")
            toroR = simpledialog.askfloat("Input", "Insira o raio da alça da caneca:")
            self.points.append(CupService.add_cup(self.points, True, cupR, cupH, toroR))
        if figure == "Tronco de Cone":
            rb = simpledialog.askfloat("Input", "Insira o raio da base do tronco de cone:")
            rs = simpledialog.askfloat("Input", "Insira o raio superior do tronco de cone:")
            h = simpledialog.askfloat("Input", "Insira a altura do tronco de cone:")
            self.points.append(ConeTrunkService.add_coneTrunk(self.points, True, rb, rs, h))


    def plot_points(self):
        if self.points:
            Plot3dImageService.plot_image(self.points)
        else:
            print("Nenhum ponto foi adicionado.")
