# Ucamp3

Descripción del Programa del Proyecto Modulo 3

1.	Definición de funciones:
- simular_maquina_galton(num_canicas, num_niveles): Esta función simula el comportamiento de una máquina de Galton. Recibe dos parámetros: num_canicas, que indica la cantidad total de canicas en la simulación, y num_niveles, que representa la cantidad de niveles u obstáculos en la máquina. La función realiza la simulación dejando caer cada canica y registra la cantidad de canicas que caen en cada contenedor. Devuelve una lista de contadores, donde cada posición de la lista representa la cantidad de canicas en ese contenedor específico.
- graficar_histograma(contadores): Esta función recibe una lista de contadores, que representa la cantidad de canicas en cada contenedor, y grafica un histograma utilizando la biblioteca Matplotlib. Muestra la cantidad de canicas en el eje y y los contenedores en el eje x. Además, agrega etiquetas a los ejes y un título al gráfico.


2.	Parámetros de la simulación:
- num_canicas = 3000: Se define el número total de canicas que se utilizarán en la simulación. En este caso, se establece en 3000.
- num_niveles = 12: Se define la cantidad de niveles u obstáculos en la máquina de Galton. En este caso, se establece en 12.

3.	Simulación:
Se llama a la función simular_maquina_galton pasando los parámetros num_canicas y num_niveles. Esta función realiza la simulación de la máquina de Galton y devuelve una lista de contadores que registra la cantidad de canicas en cada contenedor.

4.	Graficación del histograma:
Se llama a la función graficar_histograma pasando la lista de contadores obtenida de la simulación. Esta función utiliza Matplotlib para crear un gráfico de barras que representa la cantidad de canicas en cada contenedor.

El gráfico resultante muestra en el eje x los contenedores, numerados desde 0 hasta el número total de niveles. En el eje y se muestra la cantidad de canicas en cada contenedor.
o	Se agregan etiquetas a los ejes x e y, así como un título al gráfico.

En resumen, el programa simula una máquina de Galton con una cantidad específica de canicas y niveles. Luego, genera un histograma que muestra la cantidad de canicas en cada contenedor. Esto permite visualizar cómo se distribuyen las canicas a lo largo de los diferentes niveles de la máquina.
