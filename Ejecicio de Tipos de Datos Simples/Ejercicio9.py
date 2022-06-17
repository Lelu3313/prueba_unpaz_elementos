#cantidad del porcentaje anual de inversion.
cantidad = float(input("¿Cantidad a invertir? "))
interes = float (input("¿Interes porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad *(interes / 100 + 1) ** años, 2)))
