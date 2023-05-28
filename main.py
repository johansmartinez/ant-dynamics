"""from model.Hormiguero import Hormiguero
from view.InterfazHormiguero import InterfazHormiguero

alto_hormiguero = 10
ancho_hormiguero = 10
poblacion_inicial = 50
tasa_crecimiento = 0.1
tasa_muerte = 0.05
factor_generacion = 2
esperanza_vida = 10
comida_inicial = 100
tamano_inicial = 1
salud_reina = 100

hormiguero = Hormiguero(alto_hormiguero, ancho_hormiguero, poblacion_inicial, tasa_crecimiento, tasa_muerte, factor_generacion, esperanza_vida, comida_inicial, tamano_inicial, salud_reina)
hormiguero.simular_crecimiento(100)
hormiguero.mostrar_grafico()

interfaz = InterfazHormiguero(hormiguero)
interfaz.mostrar_interfaz()"""
from control.Controller import Controller

control=Controller()
control.io.ventana.mainloop()