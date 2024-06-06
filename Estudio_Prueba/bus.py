bus = [[0] * 4 for _ in range(10)]
# Asignar números de asiento automáticamente
num_asiento = 1
for fila in range(len(bus)):
    for columna in range(len(bus[0])):
        bus[fila][columna] = num_asiento
        num_asiento += 1

# Mostrar el arreglo por pantalla
for fila in bus:
    print(fila)