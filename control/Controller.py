from model.Hormiguero import Hormiguero
from view.IoManager import IoManager

class Controller:
    def __init__(self):
        self.hormiguero={}
        self.io=IoManager()
        self.ejecucion_eventos()

    def ejecucion_eventos(self):
        self.io.menu.boton_simulacion.bind("<Button-1>",self.cambiar_panel_simulacion)
        self.io.interfaz_hormiguero.boton_simular.bind("<Button-1>",self.simular)
        self.io.interfaz_hormiguero.boton_volver.bind("<Button-1>",self.volver_menu)
        self.io.menu.boton_modelo.bind("<Button-1>",self.modelo)
                                                      
    def cambiar_panel_simulacion(self, event):
        self.io.notebook.select(self.io.interfaz_hormiguero)

    def simular(self,event):
        parametros=self.io.interfaz_hormiguero.get_variables()
        self.hormiguero=Hormiguero(int(parametros[0]),int(parametros[1]),int(parametros[2]),int(parametros[3]),int(parametros[4]),int(parametros[5]),float(parametros[6]),float(parametros[7]))
        self.io.interfaz_hormiguero.mostrar_grafica(self.hormiguero.tiempo,self.hormiguero.poblacion)
    
    def volver_menu(self):
        self.io.notebook.select(self.io.menu)
    
    def modelo(self,event):
        self.io.notebook.select(self.io.modelo)