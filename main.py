import random 

elementos = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Introduce la longitud de tu contraseña segura: "))

contrasena = ""
for i in range(longitud):
    contrasena += random.choice(elementos)

print(f"Tu nueva contraseña segura es: {contrasena}")
