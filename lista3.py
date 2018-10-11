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

print("Sustituir la palabra...")
palabra = input()
print("Por la palabra...")
palabra2 = input()

if palabra in frase:
	frase = [palabra.replace(palabra, palabra2)]
else:
	print("La palabra a sustituir no está en la lista")

print(frase)