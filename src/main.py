import tkinter as tk
from tkinter import ttk
from interfaces.interface2D import Interface2DFigures
from interfaces.interface3D import Interface3D
from interfaces.interfaceMany3DFigures import InterfaceMany3DFigures
from interfaces.interfaceMany3DFiguresByCam import InterfaceMany3DFiguresByCam

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Figure Generator - Home")
        
        self.root.geometry("400x300")
        
        self.figuresButton = ttk.Button(root, text="Figuras 3D", command=self.Open3DWindow, width=30)
        self.figuresButton.pack(padx=20, pady=20, fill=tk.X)

        self.twoDFiguresButton = ttk.Button(root, text="Figuras 2D", command=self.Open2DFiguresWindow, width=30)
        self.twoDFiguresButton.pack(padx=20, pady=20, fill=tk.X)

        self.manyFiguresButton = ttk.Button(root, text="Diversas Figuras 3D", command=self.OpenMany3DFiguresWindow, width=30)
        self.manyFiguresButton.pack(padx=20, pady=20, fill=tk.X)

        self.manyFiguresButtonByCam = ttk.Button(root, text="Diversas Figuras 3D no Sistema de Coordenadas da Câmera", command=self.OpenMany3DFiguresByCamWindow, width=30)
        self.manyFiguresButtonByCam.pack(padx=20, pady=20, fill=tk.X)

        pass

    def Open3DWindow(self):
        figure3DWindow = tk.Toplevel(self.root)
        Interface3D(figure3DWindow)

    def Open2DFiguresWindow(self):
        figureWindow2DFigures = tk.Toplevel(self.root)
        Interface2DFigures(figureWindow2DFigures)

    def OpenMany3DFiguresWindow(self):
        figureWindow3DManyFigures = tk.Toplevel(self.root)
        InterfaceMany3DFigures(figureWindow3DManyFigures)

    def OpenMany3DFiguresByCamWindow(self):
        figureWindow3DManyFiguresByCam = tk.Toplevel(self.root)
        InterfaceMany3DFiguresByCam(figureWindow3DManyFiguresByCam)

def main():
    root = tk.Tk()
    MainScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()