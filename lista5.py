#usr/bin/python3
#Eliminar una plabra de la lista

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

#Crear lista 2
print("¿Cuantas palabras tiene la lista de palabras a eliminar?")
palabras2 = input()
palabras2 = int(palabras2)

frase2 = ""
frase2 = list(frase2)

x = 0

while x < palabras2:
	print("Dime la palabra ", x + 1)
	palabra = input()
	frase2.append(palabra)
	x = x + 1

print("La lista de palabras a eliminar es: ", frase2)


#Crear conjuntos para simplificar el proceso de borrado
conjunto1 = set(frase)
conjunto2 = set(frase2)

#Con esta sentencia se pueden borrar las coincidencias de la lista1 con la lista2
conjunto3 = conjunto1 - conjunto2

#Se pasa el conjunto otra vez a tipo lista
conjunto3 = list(conjunto3)

#Con este if se comprueba si ha cambiado la lista1 despues de la operacion
#Si cambia la longitud de la lista significa que se ha modificado
if len(conjunto3) == len(conjunto1):
	print("No coincide ninguna palabra")


print("La lista Ahora es: ", conjunto3)