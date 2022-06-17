#Los productos de una compra separados en lineas distintas.
cesta = input(" Introduce los productos de la cesta de la compra separados por comas: ")
print(cesta.replace(",","\n"))
#Otra manera de hacer la lista de compras.
cesta = input("Introduce los productos de la cesta de la compra separados por comas: ")
print("\n".join(cesta.split(",")))
