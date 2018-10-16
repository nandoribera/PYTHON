#usr/bin/python3
#Eliminar una plabra de la lista

#Crear lista
print("¿Cuantas palabras tiene la lista?")
palabras = input()
palabras = int(palabras)

frase = ""
frase = list(frase)

x = 0

while x < palabras:
	print("Dime la palabra ", x + 1)
	palabra = input()
	frase.append(palabra)
	x = x + 1

print("La lista creada es ", frase)

#Pedir palabra a borrar
print("Escribe la palabra que quieres borrar")
palabraBorrar = input()



while palabraBorrar not in frase and palabraBorrar != "":
	print("Escribe la palabra que quieres borrar")
	print("Si no quieres borrar ninguna palabra escribe 0")
	palabraBorrar = input()

if palabra in frase:
	while palabra in frase:
		frase.remove(palabraBorrar)

print(frase)