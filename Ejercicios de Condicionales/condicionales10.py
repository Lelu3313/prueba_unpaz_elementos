#Variedades de pizzas vegetarianas o no vegetarianas.
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el numero correspondiente al tipo de pizza que quieres: ")
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t1- Pimiento\n\t2- Tofu\n")
    ingrediente= input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end= "")
if ingrediente == "1":
    print("pimenton")
else:
    print("tofu")
    
 else:
     print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamon\n\t3- Salmon\n")
    ingredientes = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozzarella, tomate y ",end= "")
if ingredientes == "1":
    print("peperoni")
elif ingrediente == "2":
    print("jamon")
else:
    print( " salmon ")
    
    
