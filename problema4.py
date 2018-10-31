#usr/bin/env python3

def contar_vocales(cadena):
#Disminuir código de comprobación
	cadena = cadena.lower()

	#Tupla de vocales
	vocales = ("a","e","i","o","u","á","é","í","ó","ú")

	#comprobar si letra se encuentra dentro de la tupla de vocales
	contador = 0
	for x in range (len(cadena)):
		if cadena[x] in vocales:
			contador += 1
			x += 1
		else:
			x += 1

	return contador


#Introducir variable
cadena = input("Introduce una palabra o frase: ")
print("Número de vocales: ",contar_vocales(cadena))