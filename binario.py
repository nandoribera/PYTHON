print("CONVERSOR DE BINARIO A DECIMAL")
print("Introduce el número binario")
binario = input()
binario = list(binario)
binario.reverse()

x = 0
num = 0

while x < len(binario):
	if binario[x] == "1":
		num += 2 ** x
	x = x + 1

print(num)