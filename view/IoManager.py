import tkinter as tk
from tkinter import ttk
from view.Menu import Menu
from view.InterfazHormiguero import InterfazHormiguero
from view.Modelo import Modelo

class IoManager:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mi Aplicación")
        self.ventana.geometry("900x468")
        self.notebook = ttk.Notebook(self.ventana)
        self.menu=Menu(self.notebook)
        self.interfaz_hormiguero=InterfazHormiguero(self.notebook)
        self.modelo=Modelo(self.notebook)
        self.notebook.add(self.menu, text="Menu")
        self.notebook.add(self.interfaz_hormiguero,text="Simulacion")
        self.notebook.add(self.modelo,text="Modelo")
        self.notebook.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)