#usr/bin/env python3

#Función isVowel
def isVowel(char):
	#pasar parametro a lower case para disminuir el código ce comprobación
	letra = char.lower()

	#comprobar si la letra es una vocal
	if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra =="á" or letra =="é" or letra =="í" or letra =="ó" or letra =="ú":
		print(char,"es una vocal")
	else:
		print(char,"no es una vocal")


letra = input("Introduce una letra: ")
isVowel(letra)
