#usr/bin/env python3
try:
	varA = int(input("Introduce varA: "))
	varB = int(input("Introduce varB: "))


	if varA > varB:
		print ("Grande")
	elif varA == varB:
		print("igual")
	elif varA < varB:
		print("Mas pequeño")

except:
	print("Cadena involucrada")
