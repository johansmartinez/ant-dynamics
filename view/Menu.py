import tkinter as tk
from tkinter import ttk

class Menu(ttk.Frame):
    def __init__(self,notebook):
        super().__init__(notebook)
        self.boton_simulacion = tk.Button(self, text="Simulacion")
        self.boton_simulacion.pack()
        self.boton_modelo=tk.Button(self,text="Modelo")
        self.boton_modelo.pack()