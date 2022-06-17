producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitatio: "))
unidades = int(input("Introduce el numero de unidades: "))
print("{producto}: {unidades: 3d} unidades x {precio:9.2f}€ ={total:11.2f}€" . format(producto = producto, unidades = unidades,precio = precio, total =unidades * precio))
