Sistema de Reserva de Cine en Python 🎬

Estudiante: Cristian Alex Gualli Guaman
Materia: FUNDAMENTOS DE PROGRAMACION 

Objetivo del Programa

Este programa en Python simula un sistema de reservas de una sala de cine pequeña que dispone de 12 asientos distribuidos en 3 filas y 4 columnas. Permite al usuario seleccionar un asiento específico mediante las coordenadas de fila y columna y muestra el estado final de la sala.

En el sistema:

0 = Asiento libre
1 = Asiento reservado
Cómo ejecutarlo

Para ejecutar este programa, necesitas tener Python instalado en tu computadora.

Abre una terminal o consola de comandos.
Navega hasta la carpeta donde se encuentra el archivo reserva_cine.py.
Ejecuta el siguiente comando:
python reserva_cine.py

Si utilizas Windows y el comando anterior no funciona, puedes probar:

py reserva_cine.py
Funcionamiento

El programa solicita al usuario las coordenadas del asiento que desea reservar, indicando la fila y la columna. Después de realizar la reserva, se muestra el estado actualizado de la sala.

Ejemplo

Una sala inicialmente puede representarse de la siguiente manera:

0 0 0 0
0 0 0 0
0 0 0 0

Después de reservar un asiento, el estado podría ser:

0 0 1 0
0 0 0 0
0 0 0 0

Donde 1 representa el asiento que ha sido reservado.

Requisitos
Python 3.x