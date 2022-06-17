# Estoy calculando mi masa corporal, segun mi peso en kg y estatura.
peso = input("¿Cual es tu peso en kg? ")
estatura = input("¿Cual es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu indice de la masa corporal es " + str(imc))
