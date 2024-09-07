import tkinter as tk
from services.projectionService import ProjectionService

class Interface2DFigures:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface 2D com Diversas Figuras")

        # Botão para gerar a imagem
        self.plot_button = tk.Button(root, text="Gerar Imagem", command=ProjectionService.generate_image)
        self.plot_button.pack()
