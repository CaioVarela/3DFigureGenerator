import tkinter as tk
from tkinter import simpledialog, ttk
from services.plot3dImageService import Plot3dImageService
from models import cube, pyramidTrunk, cone

class Interface3D:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface 3D")
        
        self.figures = ["Cubo", "Tronco de Piramide"]  # Lista de figuras disponíveis (pode adicionar mais)
        self.points = []
        
        # Label de instruções
        self.label = tk.Label(root, text="Escolha uma figura 3D:")
        self.label.pack()

        # Combobox para selecionar a figura 3D
        self.figure_selector = ttk.Combobox(root, values=self.figures)
        self.figure_selector.pack()

        # Botão para gerar pontos automaticamente
        self.auto_fill_button = tk.Button(root, text="Preencher Coordenadas", command=self.auto_fill)
        self.auto_fill_button.pack()

        # Botão para gerar a imagem
        self.plot_button = tk.Button(root, text="Gerar Imagem", command=self.plot_points)
        self.plot_button.pack()

    def auto_fill(self):
        figure = self.figure_selector.get()
        if figure == "Cubo":
            self.add_cube()
###TODO: tronco de piramide deve virar tronco de cone, suspeito que apenas mudando a base para uma circunferencia funcione
        if figure == "Tronco de Piramide":
            self.add_pyramidTrunk()
        else:
            print("Figura não reconhecida.")

    def add_cube(self):
        l = simpledialog.askfloat("Input", "Insira o comprimento da aresta do cubo:")
        pc_x = simpledialog.askfloat("Input", "Insira a coordenada X do ponto central:")
        pc_y = simpledialog.askfloat("Input", "Insira a coordenada Y do ponto central:")
        pc_z = simpledialog.askfloat("Input", "Insira a coordenada Z do ponto central:")
        
        if l is not None and pc_x is not None and pc_y is not None and pc_z is not None:
            # Chamando o método cubo do model Cube
            x, y, z = cube.Cube.cubo(l, [pc_x, pc_y, pc_z])
            self.points.append([x, y, z])
            print(f"Cubo gerado com aresta {l} no ponto ({pc_x}, {pc_y}, {pc_z})")
        else:
            print("Valores inválidos.")
    
    def add_pyramidTrunk(self):
        lb = simpledialog.askfloat("Input", "Insira o comprimento da base maior (lb):")
        ls = simpledialog.askfloat("Input", "Insira o comprimento da base menor (ls):")
        h = simpledialog.askfloat("Input", "Insira a altura do tronco de pirâmide (h):")
        pc_x = simpledialog.askfloat("Input", "Insira a coordenada X do ponto central:")
        pc_y = simpledialog.askfloat("Input", "Insira a coordenada Y do ponto central:")
        pc_z = simpledialog.askfloat("Input", "Insira a coordenada Z do ponto central:")

        if lb is not None and ls is not None and h is not None and pc_x is not None and pc_y is not None and pc_z is not None:
            # Chamando o método tronco do model PyramidTrunk
            x, y, z = pyramidTrunk.PyramidTrunk.tronco(lb, ls, h, [pc_x, pc_y, pc_z])
            self.points.append([x, y, z])
            print(f"Tronco de pirâmide gerado com base maior {lb}, base menor {ls} e altura {h}, no ponto ({pc_x}, {pc_y}, {pc_z})")
        else:
            print("Valores inválidos.")


    def plot_points(self):
        if self.points:
            Plot3dImageService.plot_image(self.points)
        else:
            print("Nenhum ponto foi adicionado.")
