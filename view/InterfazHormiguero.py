import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class InterfazHormiguero:
    def __init__(self, hormiguero):
        self.hormiguero = hormiguero
        self.ventana = tk.Tk()
        self.ventana.title("Hormiguero")

        # Crear una figura de Matplotlib para mostrar el gráfico de la población
        self.fig_poblacion = plt.figure(figsize=(5, 3))
        self.ax_poblacion = self.fig_poblacion.add_subplot(111)
        self.ax_poblacion.set_xlabel('Tiempo')
        self.ax_poblacion.set_ylabel('Población')
        self.ax_poblacion.set_title('Gráfico de la Población')
        self.linea_poblacion, = self.ax_poblacion.plot([], [])

        # Crear un lienzo para mostrar el gráfico de la población en la ventana
        self.canvas_poblacion = FigureCanvasTkAgg(self.fig_poblacion, master=self.ventana)
        self.canvas_poblacion.draw()
        self.canvas_poblacion.get_tk_widget().pack(side=tk.LEFT)

        # Crear una figura de Matplotlib para mostrar la animación
        self.fig_animacion = plt.figure(figsize=(5, 5))
        self.ax_animacion = self.fig_animacion.add_subplot(111)
        self.ax_animacion.set_xlim(0, self.hormiguero.ancho)
        self.ax_animacion.set_ylim(0, self.hormiguero.alto)
        self.puntos_hormigas = self.ax_animacion.scatter([], [], color='black', marker='o')
        self.punto_reina = self.ax_animacion.scatter([], [], color='red', marker='s')

        # Crear un lienzo para mostrar la animación en la ventana
        self.canvas_animacion = FigureCanvasTkAgg(self.fig_animacion, master=self.ventana)
        self.canvas_animacion.draw()
        self.canvas_animacion.get_tk_widget().pack(side=tk.LEFT)

    def mostrar_interfaz(self):
        # Mostrar el gráfico de la población

        # Ejecutar la animación
        self.animacion = animation.FuncAnimation(self.fig_animacion, self.actualizar_animacion, frames=10, interval=500)
        self.ventana.mainloop()

    def actualizar_animacion(self, frame):
        # Generar posiciones aleatorias para las hormigas (excepto la reina)
        #TODO: cambiar
        posiciones_x = np.random.randint(0, self.hormiguero.ancho, 100 )
        posiciones_y = np.random.randint(0, self.hormiguero.alto, 100 )

        # Posición fija para la hormiga reina
        reina_x, reina_y = self.hormiguero.ancho/2, self.hormiguero.alto/2

        # Actualizar las posiciones en la animación
        self.puntos_hormigas.set_offsets(np.column_stack((posiciones_x, posiciones_y)))
        self.punto_reina.set_offsets(np.column_stack((reina_x, reina_y)))

        # Redibujar la animación
        self.canvas_animacion.draw()
