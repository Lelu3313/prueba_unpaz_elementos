# se le preguentar a el usuario sobre la renta.
renta = float(input("¿Cual es tu renta anual? "))
# condicional para determinar el tipo impositivo dependiendo de la renta.
if renta< 10000:
    tipo = 5
elif renta < 20000:
    tipo =15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
#producto de la renta.
    print ("Tienes que pagar" , renta * tipo / 100, "€" ,sep="")
