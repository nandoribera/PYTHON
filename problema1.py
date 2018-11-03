#usr/bin/env python3

#Comprobar si se introduce un int
try:
	varA = int(input("Introduce varA: "))
	varB = int(input("Introduce varB: "))

#Comparativa de excepciones
	if varA > varB:
		print ("Grande")
	elif varA == varB:
		print("igual")
	elif varA < varB:
		print("Mas pequeño")

#Excepción, si una de las variables es str se producirá la siguente excepción.
except:
	print("Cadena involucrada")
