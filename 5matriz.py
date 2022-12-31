#Matriz simétrica

print("Ingrese el orden de la matriz a calcular ")
filasA,columnasA=int(input()),int(input())

contador =0

if columnasA ==filasA :
    matrizA=[]
    for i in range (filasA):
        matrizA.append([0] * columnasA)
    
    print("Ingrese la matriz A")
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(input(f"ingrese la posicion número {fila},{columna}: "))

    for fila in range(filasA):
        for columna in range(columnasA):
            normal = matrizA[fila][columna]
            transpuesta=matrizA[columna][fila]
            if normal == transpuesta:
                contador += 1
    
    if contador == (filasA * columnasA):
        print("La matriz es simetrica ")
    else:
        print("La matriz No es simétrica ")
else:
    print("La matriz no es simétrica")

   