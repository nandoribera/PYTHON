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

#Crear lista 2 al reves de la primera
frase2 = frase
#Ponerla al reves
frase2.reverse()

print("La lista inversa es: ", frase2)