# ==========================================
# Programa de Gestión de Reservas de Cine
# ==========================================

# Crear la matriz de 3 filas por 4 columnas inicializada en 0 (asientos libres)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila y columna que desea reservar
print("--- SISTEMA DE RESERVA DE ASIENTOS ---")
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:
            
 # Marcar el asiento como reservado asignándole el valor 1
            asientos[fila][columna] = 1
            print("\n¡Reserva exitosa!")
            
else:
            print("\nError: Asiento inexistente. La fila debe ser de 0 a 2 y la columna de 0 a 3.")

# Mostrar el estado completo de la sala utilizando bucles anidados
print("\nEstado de la sala:")

# Bucle externo para recorrer las filas (i)
for i in range(3):
    # Bucle interno para recorrer las columnas (j)
    for j in range(4):
        # Imprime el valor del asiento sin salto de línea y con un espacio para formato de tabla
        print(asientos[i][j], end=" ")
    # Salto de línea al terminar cada fila
    print()