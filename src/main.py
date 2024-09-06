import tkinter as tk
from tkinter import ttk
from interfaces.interface3D import Interface3D
from interfaces.interfaceMany3DObjects import InterfaceMany3DObjects
##from interfaces.LineInterface import LineInterface
##from interfaces.PolygonInterface import PolygonInterface  
##from interfaces.HermiteCurveInterface import HermiteCurveInterface

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Figure Generator - Home")
        
        self.root.geometry("400x200")
        
        self.lineButton = ttk.Button(root, text="Figuras 3D", command=self.Open3DWindow, width=30)
        self.lineButton.pack(padx=20, pady=20, fill=tk.X)

        self.curveButton = ttk.Button(root, text="Figuras 2D - WIP", command=self.OpenPolygonWindow, width=30)
        self.curveButton.pack(padx=20, pady=20, fill=tk.X)

        self.polygonButton = ttk.Button(root, text="Diversas Figuras 3D", command=self.OpenMany3DObjectsWindow, width=30)
        self.polygonButton.pack(padx=20, pady=20, fill=tk.X)

        pass

    def Open3DWindow(self):
        figure3DWindow = tk.Toplevel(self.root)
        Interface3D(figure3DWindow)

    def OpenPolygonWindow(self):
        ###2DFigures
        return

    def OpenMany3DObjectsWindow(self):
        figureWindow3DManyObjects = tk.Toplevel(self.root)
        InterfaceMany3DObjects(figureWindow3DManyObjects)

def main():
    root = tk.Tk()
    MainScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()