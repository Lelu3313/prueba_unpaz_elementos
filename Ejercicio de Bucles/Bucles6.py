# El programa pide al usuario un numero entero y muestra un triangulo.
n = int(input(" Introduce la altura del triangulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
