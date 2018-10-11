for i in [0,1,2,3,4]:
	print(i)

for i in (0,1,2,3,4):
	print(i)
for i in {0,1,2,3,4}:
	print(i)
#el conjunto no puede especificar el orden 
for i in {4,3,2,1,0}:
	print(i)
#Mal uso del tipo de dato
for i in "01234":
	print(i)