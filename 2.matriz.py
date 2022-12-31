#2. Multiplicación de matrices.


print("Ingrese el orden de la matriz A ")
filasA,columnasA= int(input()),int(input())

print("Ingrese el orden de la matriz B ")
filasB,columnasB= int(input()),int(input())

#Se ejecuta si es posible hacer la multiplicación
if columnasA == filasB:
    #crear la matriz A con el tamaño filasA * columnasA
    matrizA=[]
    for i in range(filasA):
        matrizA.append([0] * columnasA)
        
    #crear la matriz B con el tamaño filasB * columnasB
    matrizB=[]
    for i in range(filasB):
        matrizB.append([0] * columnasB)

#RELLENAMOS LA MATRIZ A
    print("Ingrese la matriz A")
    for filas in range (filasA):
        for columnas in range(columnasA):
            matrizA[filas][columnas] = float(input(f"ingresa la posición numero {filas},{columnas} de la matriz A= "))
#RELLENAMOS LA MATRIZ B
    print("Ingrese la matriz B")
    for filas in range (filasB):
        for columnas in range(columnasB):
            matrizB[filas][columnas] = float(input(f"ingresa la posición numero {filas},{columnas} de la matriz B= "))

#CREAMOS LA MATRIZ C O RESULTANTE DE TAMAÑO FILAS A * COLUMNAS B
    matrizC =[]
    for i  in range(filasA):
        matrizC.append([0]*columnasB)

#PRODUCTO DE MATRICES
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizB)):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

    print("EL PRODUCTO DE MATRICES ES :")
    for i in matrizC:
        print(i)
else:
    print("Matriz Erróneo ")
