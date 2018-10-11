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

print("¿Que palabra buscas?")
palabra = input()

num = frase.count(palabra)

if num > 0:
	print("La palabra", palabra,"aparece ", num, " veces en la lista.")
else:
	print("La palabra", palabra,"no aparece en la lista.")