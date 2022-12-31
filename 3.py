#Crea un array o arreglo unidimensional donde le indiques
# el tamaño por teclado y crear una función que rellene
# el array o arreglo con los múltiplos de un número pedido
# por teclado.
# Por ejemplo, si defino un array de tamaño 5 y elijo un
# 3 en la función, el array contendrá 3, 6, 9, 12, 15.
# Muéstralos por pantalla usando otra función distinta.



n = int(input(u"Ingrese el tamaño del arreglo: "))
m = int(input(u"Ingrese el número del que desea sus múltiplos: "))
ARREGLO = []
for i in range (0,n):
    ARREGLO.append(i*m)
print(ARREGLO)
