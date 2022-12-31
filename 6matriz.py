#determinante de una matriz

import numpy as np

print("Ingrese el orden de la matriz a calcular ")
filasA , columnasA= int(input()), int(input())
#creamos la matriz
matrizA = []
for i in range (filasA):
    matrizA.append([0] * columnasA)
    
#rellenams los datos
print("Ingrese la matriz A")
for fila in range(filasA):
    for columna in range(columnasA):
        matrizA[fila][columna] = float(input(f"ingrese la posicion número {fila},{columna}: "))

determinante =np.linalg.det(matrizA)
print(determinante)