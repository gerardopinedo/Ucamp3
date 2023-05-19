import random
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_niveles):
    contadores = [0] * (num_niveles + 1)  # Inicializar los contadores de los contenedores

    for _ in range(num_canicas):
        posicion = num_niveles // 2  # Iniciar en el nivel central

        for _ in range(num_niveles):
            if random.random() < 0.5:  # Decidir si la canica cae a la izquierda o derecha
                posicion -= 1
            else:
                posicion += 1
            if posicion < 0:  # Ajustar la posición si se sale del rango
                posicion = 0
            elif posicion > num_niveles:  # Ajustar la posición si se sale del rango
                posicion = num_niveles

        contadores[posicion] += 1  # Incrementar el contador del contenedor correspondiente

    return contadores

def graficar_histograma(contadores):
    num_contenedores = len(contadores)
    niveles = list(range(num_contenedores))

    plt.bar(niveles, contadores)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de canicas')
    plt.title('Histograma de la Máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
num_niveles = 12

# Simulación
resultados = simular_maquina_galton(num_canicas, num_niveles)

# Graficación del histograma
graficar_histograma(resultados)
