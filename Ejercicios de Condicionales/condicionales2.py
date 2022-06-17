# Es un programa que guarda la contraseña de un usuario.
key = " contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")
