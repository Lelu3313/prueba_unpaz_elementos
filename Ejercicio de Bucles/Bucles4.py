#CUENTA LOS NUMEROS POSITIVOS DE ATRAS DESDE EL NUMERO ELEGIDO HASTA CERO.
n = int(input("Introduce un numero entero positivo: "))
for i in range(n , -1 , -1):
    print( i, end= "," )
