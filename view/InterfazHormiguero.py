import tkinter as tk
from tkinter import ttk

class InterfazHormiguero(ttk.Frame):

    def __init__(self,notebook):
        super().__init__(notebook)
        self.alto_hormiguero = ttk.Entry()
        self.alto_hormiguero.pack()
        """self.ancho_hormiguero = tk.Entry()
        self.poblacion_inicial = tk.Entry()   
        self.tasa_crecimiento = tk.Entry()
        self.tasa_muerte = tk.Entry()
        self.factor_generacion = tk.Entry()
        self.esperanza_vida = tk.Entry()
        self.comida_inicial = tk.Entry()
        self.tamano_inicial = tk.Entry()
        self.salud_reina = tk.Entry()

    def ubicar_componentes(self):
        self.alto_hormiguero.place(x=0,y=0)"""