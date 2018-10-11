#Listas1
#Pedir el número de palabras de la lista
print("¿Cuantas palabras tiene la lista?")
palabras = input()

#Convertir el str a int para obtener el tamaño de la lista
palabras = int(palabras)

#iniciar lista y crearla
frase = ""
frase = list(frase)

#Indice de la función
x = 0

#funcion para introducir las palabras dependiendo 
#del número introduucido en el primer paso
while x < palabras:
	print("Dime la palabra ", x + 1)
	palabra = input()
	#añadir la palabra a la lista
	frase.append(palabra)
	x = x + 1

#Iniciar el número de respuesta
respuesta = 0

#funcion de comprobacion del número de palabras en la lista
while respuesta != palabras:
	print("¿Cuantas palabras tiene la lista?")
	respuesta = input()
	respuesta = int(respuesta)
	#comprobar que la respuesta es correcta, si coincide el int de
	#la respuesta con el numero de palabras introducido en el primer paso
	if respuesta != palabras:
		print("Imposible!")

print("¡Correcto!")
print(frase)
