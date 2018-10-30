#usr/bin/python3
#Eliminar una plabra de la lista

#Crear lista
print("¿Cuantas palabras tiene la lista?")
palabras = input()
palabras = int(palabras)

frase = ""
frase = list(frase)

x = 0

while x < palabras:
	print("Dime la palabra ", x + 1)
	palabra = input()
	frase.append(palabra)
	x = x + 1

print("La lista creada es ", frase)

#Pedir palabra a borrar
print("Escribe la palabra que quieres borrar")
print("O pulsa intro si no quieres borrar ninguna")
palabraBorrar = input()


#Si la palabra borrar no coincide con ninguna de la lista pide otra vez una palabra
#Si no se quiere borrar ninguna palabra bastara con pulsar intro
while palabraBorrar not in frase and palabraBorrar != "":
	print("Escribe la palabra que quieres borrar")
	print("Si no quieres borrar ninguna palabra pulsa intro")
	palabraBorrar = input()

#Con este loop se busca todas las coincidencias de la palabra a borrar en la lista
#si no, solo borraria la primera coincidencia
if palabraBorrar in frase:
	while palabraBorrar in frase:
		frase.remove(palabraBorrar)

print(frase)