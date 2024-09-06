import tkinter as tk
from services.plot3dImageService import Plot3dImageService
from models import cube, pyramidTrunk, cone, cylinder
from services import translationService

class InterfaceMany3DObjects:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface 3D com Diversos Objetos")

        # Botão para gerar a imagem
        self.plot_button = tk.Button(root, text="Gerar Imagem", command=self.select_object)
        self.plot_button.pack()

    def select_object(self):
        self.points = []

        self.add_box()
        self.add_cone()
        self.add_pipe()
        self.add_cup()
        self.add_coneTrunk()

        self.plot_points()

        self.points = []

        self.add_box(False)
        self.add_cone(False)
        self.add_pipe(False)
        self.add_cup(False)
        self.add_coneTrunk(False)

        self.plot_points()

    def add_box(self, isCentralized=True):
        x, y, z = cube.Cube.cubo(2, [0, 0, 0])

        if (isCentralized == False):
            points = translationService.TranslationService.translacao(8, 8, 8, [x, y, z])
            self.points.append(points)
        else: 
            self.points.append([x, y, z])

    def add_cone(self, isCentralized=True):
        x, y, z = cone.Cone.cone(2, 3*2, [0, 0, 0])
        
        if (isCentralized == False):
            points = translationService.TranslationService.translacao(2, 4, 0, [x, y, z])
            self.points.append(points)
        else: 
            self.points.append([x, y, z])

    def add_pipe(self, isCentralized=True):
        x, y, z = cylinder.Cylinder.cilindro(2, [0, 0, 0], p=1/5)
        
        if (isCentralized == False):
            points = translationService.TranslationService.translacao(6, 4, 4, [x, y, z])
            self.points.append(points)
        else: 
            self.points.append([x, y, z])
    
    def add_cup(self, isCentralized=True):
        print("mb de chapeuzim")
        
    def add_coneTrunk(self, isCentralized=True):
        x, y, z = pyramidTrunk.PyramidTrunk.tronco(5, 3, 2, [0, 0, 0], 1/5)

        if (isCentralized == False):
            points = translationService.TranslationService.translacao(-3, -3, -3, [x, y, z])
            self.points.append(points)
        else: 
            self.points.append([x, y, z])


    def plot_points(self):
        if self.points:
            Plot3dImageService.plot_image(self.points)
        else:
            print("Nenhum ponto foi adicionado.")
