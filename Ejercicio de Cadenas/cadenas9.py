fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print("Dia" , fecha[:2])
print("Mes" , fecha[3:5])
print("Año" , fecha[6:])

fecha = input("Introduce la fecha de tu nacimiento en formato dia/mes/año: ")
dia = fecha[:fecha.find("/")+1:]
mesaño = fecha[fecha.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]
print("Dia" , dia)
print("Mes" , mes)
print("Año" , año)
