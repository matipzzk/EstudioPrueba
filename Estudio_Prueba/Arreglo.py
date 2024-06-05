# Creamos un arreglo/Matriz 3x3x3

arreglo = [["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"]],
[["Blanco", "amarillo", "rojo"], ["Naranja", "Verde", "Blanco"], ["amarillo", "rojo", "Naranja"]],
[["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"], ["Blanco", "amarillo", "rojo"]]

# Iniciamos Los contadores 

contado_amarillo = 0
contado_rojo = 0
contado_naranja = 0
contado_verde = 0
contado_blanco = 0

# Recorro y cuento colores  
# Recorro la matriz de 3x3x3
# Verifica cuantas veces se repite cada color en la matriz



for i in range(3):
    for j in range(3):
        for k in range(3):
            if arreglo[i][j][k] == "amarillo":
                contado_amarillo += 1
            elif arreglo[i][j][k] == "rojo":
                contado_rojo += 1
            elif arreglo[i][j][k] == "Naranja":
                contado_naranja += 1
            elif arreglo[i][j][k] == "Verde":
                contado_verde += 1
            elif arreglo[i][j][k] == "Blanco":
                contado_blanco += 1