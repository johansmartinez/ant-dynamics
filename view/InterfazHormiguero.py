import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class InterfazHormiguero(ttk.Frame):

    def __init__(self,notebook):
        super().__init__(notebook)
        self.poblacion_inicial_txt = tk.Entry(self)
        self.poblacion_inicial_lbl=tk.Label(self,text="Poblacion inicial")
        self.dias_simulacion_txt = tk.Entry(self)
        self.dias_simulacion_lbl= tk.Label(self,text="Dias a simular")
        self.vida_media_hormiga_reina_txt = tk.Entry(self)
        self.vida_media_hormiga_reina_lbl=tk.Label(self,text="Vida media H reyna")
        self.tamanio_hormiguero_txt = tk.Entry(self)
        self.tamanio_hormiguero_lbl=tk.Label(self,text="Tamaño del hormiguero")
        self.comida_inicial_txt = tk.Entry(self)
        self.comida_inicial_lbl=tk.Label(self,text="Comida inicial")
        self.max_huevos_esp_txt = tk.Entry(self)
        self.max_huevos_esp_lbl= tk.Label(self,text="Factor de generacion")
        self.tasa_muerte_txt = tk.Entry(self)
        self.tasa_muerte_lbl=tk.Label(self,text="Tasa de muerte")     
        self.tasa_enfermedad_txt = tk.Entry(self)
        self.tasa_enfermedad_lbl=tk.Label(self,text="Tasa de enfermedad")
        self.boton_simular=tk.Button(self,text="Simular")
        self.boton_volver=tk.Button(self,text="Volver")
        self.graph_frame = ttk.Frame(self)
        self.graph_frame.place(x=300,y=25)
        self.ubicar_componentes()
        
    def ubicar_componentes(self):
        self.poblacion_inicial_lbl.place(x=20,y=25)
        self.poblacion_inicial_txt.place(x=200,y=25)
        self.dias_simulacion_lbl.place(x=20,y=65)
        self.dias_simulacion_txt.place(x=200,y=65)
        self.vida_media_hormiga_reina_lbl.place(x=20,y=105)
        self.vida_media_hormiga_reina_txt.place(x=200,y=105)
        self.tamanio_hormiguero_lbl.place(x=20,y=145)
        self.tamanio_hormiguero_txt.place(x=200,y=145)
        self.comida_inicial_lbl.place(x=20,y=185)
        self.comida_inicial_txt.place(x=200,y=185)
        self.max_huevos_esp_lbl.place(x=20,y=225)
        self.max_huevos_esp_txt.place(x=200,y=225)
        self.tasa_muerte_lbl.place(x=20,y=265)
        self.tasa_muerte_txt.place(x=200,y=265)
        self.tasa_enfermedad_lbl.place(x=20,y=305)
        self.tasa_enfermedad_txt.place(x=200,y=305)
        self.boton_volver.place (x=100,y=365)
        self.boton_simular.place(x=180,y=365)
    
    def mostrar_grafica(self,x,y):
        fig = plt.figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        # Crear el lienzo de la figura para tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        # Colocar el lienzo en el frame
        canvas.get_tk_widget().place(x=300,y=25)
        
    def get_variables(self):
        return [self.poblacion_inicial_txt.get(),self.dias_simulacion_txt.get(),self.vida_media_hormiga_reina_txt.get(),self.tamanio_hormiguero_txt.get(),self.comida_inicial_txt.get(),self.max_huevos_esp_txt.get(),self.tasa_muerte_txt.get(),self.tasa_enfermedad_txt.get()]
        