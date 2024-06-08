import os 
# Matriz de 3x4
matriz = [[0]*4 for i in range(3)]


# Ingresa los valors de la matriz según usuario 
for i in range(3):
    for j in range(4):
        matriz[i][j] = int(input(f"Ingrese el número [{i}][{j}]: "))

# imprime la matriz 
for i in range (3):
    for j in range(4):
        print(matriz[i][j], end = " ")
    print()