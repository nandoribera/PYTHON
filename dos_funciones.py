#usr/bin/env python3

print("Calculo del area de un triangulo: ")

print("Para calcular el area y la base del triangulo se introducen" 
	"dos valores, la base y la altura.")

#Función area
def area_triangulo(base,altura):
	#El area es base por altura partido 2
	area = (base * altura) /2
	#return del area
	return area

#Función segmentos
def longitud_seg(*segmentos):
	suma = 0
	for segmento in segmentos:
		suma = segmento + suma
	return suma
	
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
	
print("Ahora se va a calcular el perimetro suponiendo que el "
"triangulo es un triangulo rectangulo")

print("calculando el tercer lado del triangulo mediante el teorema de Pitagoras "
"h = raiz cuadrada de base elevada a 2 + altura elevada a 2")

#Importar operación raiz cuadrada
from math import sqrt
h = sqrt(base**2 + altura**2)


perimetro = longitud_seg(base,altura,h)
print("La longitud de los segmentos(perimetro) es:",perimetro)

#Pausa en CMD windows
input("Pulsa INTRO para continuar...")


