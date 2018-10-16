#usr/bin/python3
#Sustituir valor de una lista

#Crear Lista
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



#Pedir la palabra a sustituir
print("Sustituir la palabra...")
palabra = input()


#Si la palabra no esta en la lista pedirla de nuevo
while palabra not in frase:
	print("La palabra no esta en la lista")
	print("------------------------------")
	

	#Pedir otra vez la palabra a sustituir en el while hasta que se encuentre
	print("Sustituir la palabra...")
	palabra = input()



#Pedir la palabra sustituta
print("Por la palabra...")
palabra2 = input()


#Se sustituye palabra por palabra2 con este comando
frase = [pal.replace(palabra, palabra2) for pal in frase]


print(frase)
