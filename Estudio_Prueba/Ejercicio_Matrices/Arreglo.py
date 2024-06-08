# Creamos un arreglo/Matriz 3x3x3

arreglo = [
    [["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"]],
    [["Blanco", "amarillo", "rojo"], ["Naranja", "Verde", "Blanco"], ["amarillo", "rojo", "Naranja"]],
    [["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"], ["Blanco", "amarillo", "rojo"]]
]

# Iniciamos Los contadores 

contado_amarillo = 0
contado_rojo = 0
contado_naranja = 0
contado_verde = 0
contado_blanco = 0

# Recorro y cuento colores  
# Recorro la matriz de 3x3x3
# Verifica cuantas veces se repite cada color en la matriz



for x in range(3):
    for y in range(3):
        for k in range(3):
            if arreglo[x][y][k] == "amarillo":
                contado_amarillo += 1
            elif arreglo[x][y][k] == "rojo":
                contado_rojo += 1
            elif arreglo[x][y][k] == "Naranja":
                contado_naranja += 1
            elif arreglo[x][y][k] == "Verde":
                contado_verde += 1
            elif arreglo[x][y][k] == "Blanco":
                contado_blanco += 1
                
# Muestro Los Resultados de cada color
print(f"Número de veces que repite el color 'Amarillo': {contado_amarillo}")
print(f"Número de veces que repite el color 'Rojo': {contado_rojo}")
print(f"Número de veces que repite el color 'Naranja': {contado_naranja}")
print(f"Número de veces que repite el color 'Verde': {contado_verde}")
print(f"Número de veces que repite el color 'Blanco': {contado_blanco}")
