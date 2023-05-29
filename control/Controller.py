from model.Hormiguero import Hormiguero
from view.IoManager import IoManager

class Controller:
    def __init__(self):
        self.hormiguero={}
        self.io=IoManager()
        self.ejecucion_eventos()

    def ejecucion_eventos(self):
        self.io.menu.boton_simulacion.bind("<Button-1>",self.cambiar_panel_simulacion)

    def cambiar_panel_simulacion(self, event):
        self.io.notebook.select(self.io.interfaz_horiguero)