import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def update(frame):
    # Generar posiciones aleatorias para las hormigas (excepto la reina)
    posiciones_x = np.random.randint(0, ancho, poblacion - 1)
    posiciones_y = np.random.randint(0, alto, poblacion - 1)

    # Posición fija para la hormiga reina
    reina_x, reina_y = ancho/2, alto/2

    # Limpiar el gráfico
    plt.clf()

    # Dibujar el hormiguero y las hormigas
    plt.scatter(posiciones_x, posiciones_y, color='black', marker='o', label='Hormigas')
    plt.scatter(reina_x, reina_y, color='red', marker='s', label='Hormiga Reina')
    plt.xlim(0, ancho)  # Límites del eje x
    plt.ylim(0, alto)  # Límites del eje y
    plt.gca().set_aspect('equal', adjustable='box')  # Aspecto cuadrado
    plt.legend()  # Mostrar leyenda

# Tamaño del hormiguero
alto, ancho = 10, 10

# Tamaño de la población de hormigas
poblacion = 50

# Crear una figura
fig = plt.figure(figsize=(5, 5))

# Animación
ani = FuncAnimation(fig, update, frames=10, interval=500)

# Mostrar la animación
plt.show()
