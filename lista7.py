#Crear lista 1
print("¿Cuantas palabras tiene la primera lista?")
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

print("La lista creada es: ", frase)

#Con el comando set se crea un conjunto sin valores repetidos
sinRepetidos = set(frase)

#Se vuelve a transformar en lista
sinRepetidos = list(sinRepetidos)

#Este if comprueba si la lista sufre alguna modificacion de longitud
if len(sinRepetidos) == len(frase):
	print("Ninguna repeticion, la lista es: ", sinRepetidos)

else:
	print("La lista sin repeticiones es: ", sinRepetidos)