import tkinter as tk
from tkinter import ttk

class Menu(ttk.Frame):
    def __init__(self,notebook):
        super().__init__(notebook)
        self.boton_simulacion = tk.Button(self, text="Simulacion",width=20,height=4)
        self.boton_simulacion.place(x=600,y=75)
        self.boton_modelo=tk.Button(self,text="Modelo",width=20,height=4)
        self.boton_modelo.place(x=600,y=175)
        self.proyecto=tk.Label(self,text="SIMULACION POR DINAMICA DE SISTEMAS\n DE UN HORMIGUERO CONTROLADO")
        self.proyecto.place(x=80,y=40)
        self.integrantes=tk.Label(self,text="INTEGRANTES:\n\nLuis Miguel Avella Avila\nJohan Sebastian Marniez Junco\nAndres Felipe Cañas Carrillo\nSantiago Moreno")
        self.integrantes.place(x=110,y=100)


    