num = int(input("introduce un numero: "))
if num%2 == 0:
	print("Es divisible por 2")
elif num%3 == 0:
	print("Esdivisible por 3")
elif num%5 == 0:
	print("Es divisible por 5")
else:
	print("No esdivisible por 2, 3 o 5")