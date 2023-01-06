#Dada las siguientes notas almacenadas en un arreglo:
# [20, 15, 12, 11, 8, 4, 1]
# Elimine la nota más baja programáticamente sin usar la
# función (min) y escriba en pantalla.
# Luego programáticamente calcule el promedio de notas
# descontando la nota eliminada.

A = [20, 15, 12, 11, 8, 4, 1]
maximo = 20

for i in A:
    if i<maximo:
        maximo=i
print ("La nota mas baja es:",maximo)
A.remove(maximo)
suma = 0
for j in A:
    suma+=j
print ("La suma de las notas",suma)
print ("El promedio de las notas restantes es ", suma/len(A))
print ("la nota redondeado seria ", suma//len(A))









