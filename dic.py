dic = {'piso1' : 'Juan', 'piso2' : 'Pepe'} 
for k,v in dic.items():
	print(k,v)

print("*************")
for i,v in enumerate(['a', 'b', 'c']):
	print(i,v)

print("*************")
preguntas =['nombre','apellido','dirección']
datos = ['pepe','lopez','Madrid']
for i,v in zip(preguntas, datos):
	print(i,v)

print("*************")
for i in reversed([0,1,2,3,4]):
	print(i)

print("*************")
for i in sorted([0,3,2,4,1]):
	print(i)

print("*************")
for i in range(1,50): 
	primo = True
	for k in range(2,i):
		if (i%k) == 0:
			print(i, " es divisible por", k)
			primo = False
	if primo:
		print(i, "es primo")