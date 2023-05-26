import numpy as np
import matplotlib.pyplot as plt

class Hormiguero:
    def __init__(self,alto_hormiguero, ancho_hormiguero, poblacion_inicial, tasa_crecimiento, tasa_muerte, factor_generacion, esperanza_vida, comida_inicial, tamano_inicial, salud_reina):
        self.poblacion = [poblacion_inicial]
        self.alto=alto_hormiguero
        self.ancho=ancho_hormiguero
        self.tasa_crecimiento = tasa_crecimiento
        self.tasa_muerte = tasa_muerte
        self.factor_generacion = factor_generacion
        self.esperanza_vida = esperanza_vida
        self.comida = [comida_inicial]
        self.tamano = [tamano_inicial]
        self.salud_reina = [salud_reina]
        self.fig_poblacion = plt.figure(figsize=(5, 3))

    def simular_crecimiento(self, pasos):
        for _ in range(pasos):
            poblacion_actual = self.poblacion[-1]
            nueva_cria = poblacion_actual * self.factor_generacion
            nuevo_crecimiento = poblacion_actual * self.tasa_crecimiento
            muertes = poblacion_actual * self.tasa_muerte

            poblacion_nueva = poblacion_actual + nueva_cria + nuevo_crecimiento - muertes
            self.poblacion.append(poblacion_nueva)

            comida_actual = self.comida[-1]
            comida_nueva = poblacion_nueva * 0.1  # Por ejemplo, se añade un 10% de la población como comida
            comida_consumida = poblacion_actual * 0.05  # Por ejemplo, cada hormiga consume un 5% de comida
            comida_disponible = comida_actual + comida_nueva - comida_consumida
            self.comida.append(comida_disponible)

            tamano_actual = self.tamano[-1]
            tamano_nuevo = tamano_actual + (poblacion_nueva - poblacion_actual) * 0.01  # Por ejemplo, cada nueva hormiga aumenta el tamaño en un 1%
            self.tamano.append(tamano_nuevo)

            salud_reina_actual = self.salud_reina[-1]
            if poblacion_nueva > 1000:  # Por ejemplo, si la población supera cierto umbral, se genera una nueva hormiga reina
                salud_reina_nueva = salud_reina_actual - 0.1  # Por ejemplo, la salud de la nueva hormiga reina disminuye en 0.1
                poblacion_nueva -= 1  # Restamos 1 a la población debido a la generación de la nueva hormiga reina
            else:
                salud_reina_nueva = salud_reina_actual
            self.salud_reina.append(salud_reina_nueva)
            self.poblacion[-1] = poblacion_nueva

    def mostrar_grafico(self):
        tiempo = np.arange(len(self.poblacion))
        plt.plot(tiempo, self.poblacion, label='Población')
        plt.plot(tiempo, self.comida, label='Comida')
        plt.plot(tiempo, self.tamano, label='Tamaño')
        plt.plot(tiempo, self.salud_reina, label='Salud de la Reina')
        plt.xlabel('Tiempo')
        plt.ylabel('Cantidad')
        plt.title('Crecimiento del hormiguero')
        plt.legend()
        plt.show()


