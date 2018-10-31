#usr/bin/env python3


#Función isVowel2
def isVowel2(char):

	#Disminuir código de comprobación
	letra = char.lower()

	#Tupla de vocales
	vocales = ("a","e","i","o","u")

	#comprobar si letra se encuentra dentro de la tupla de vocales
	if letra in vocales:
		print(char,"es una vocal")
	else:
		print(char,"no es una vocal")


#Introducir variable
letra = input("Introduce una letra: ")
isVowel2(letra)
