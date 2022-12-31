#Hallar la matriz transpuesta

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


print("\nMatriz Inicial\n")
for i in matrizA:
    print(i)

filasB =columnasA
columnasB=filasA

matrizB=[]
for i in range(filasA):
    matrizB.append([0] * columnasA)

#calculando la matriz transpuesta.

for fila in range(filasB):
    for columna in range(columnasB):
        matrizB[fila][columna]= matrizA[columna][fila]


print("\n Matriz Transpuesta\n")
for i in matrizB:
    print(i)



