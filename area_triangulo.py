#usr/bin/env python3

#Funcion para hallar el area de un triangulo
def area_triangulo(base,altura):
	#El area es base por altura partido 2
	area = (base * altura) /2
	#return del area
	return area



"""El usuario uintroduce la base y la altura del triangulo.

Se realiza un try para comprobar la introducción de los valores
de las variables, el programa contempla la introducción de float"""
try:
	base = float(input("Introduzca la base: "))
	altura = float(input("Introduzca la altura: "))

	print("Llamada a la función con los valores de base y altura.")
	#Llamada a la función con los parámetros de base y altura
	area = area_triangulo(int(base),int(altura))

	print("Calculando área... ")
	
	#Imprime area
	print("El área del triangulo es ",area)

#Resultado de la excepción
except ValueError:
    print("!Debes introducir un número!")

