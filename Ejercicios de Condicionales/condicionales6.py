#Los alumnos de un curso se dividen en dos grupos A Y B.
name = input("¿Como te llamas?")
gender = input("¿Cual es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < "m") or (gender == "H" and name.lower() > "n"):
    group = "A"
else:
    group = "B"
    print("Tu grupo es " + group)
    

                
