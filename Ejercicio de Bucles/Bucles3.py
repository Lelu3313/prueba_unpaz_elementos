#Pide el programa un numero entero positivo y muestra los numeros impares desde 1.
n = int(input("Introduce un numero entero positivo: " ))
for i in range(1, n+1, 2):
    print(i, end=" , ")
    
