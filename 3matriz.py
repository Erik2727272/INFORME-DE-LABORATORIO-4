#Calcular la diagonal principal de una matriz
print("Ingrese el orden de la matriz a calcular ")
filasA,columnasA=int(input()),int(input())

diagonal =0
if filasA == columnasA:
    matrizA=[]
    for i in range (filasA):
        matrizA.append([0] * columnasA)
    
    print("Ingrese la matriz A")
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(input(f"ingrese la posicion número {fila},{columna}: "))

    for fila in range(filasA):
        for columna in range(columnasA):
            if fila == columna:
                diagonal += matrizA[fila][columna]
    print(f"El valor de la diagonal principal es: {diagonal} ")
