#Función longitud variable de segmentos
def longitud_seg(segmentos):
	suma = 0
	for x in range(len(segmentos)):
		suma = int(segmentos[x]) + suma
	return suma


segmentos = []
segmento = -1

print("Introduzca los segmentos, para terminar introduzca 0")

x = 1
while segmento != '0':
	print("Dime la longitud del segmento",x,":")
	segmento = input()
	segmentos.append(segmento)
	x += 1



longitud = longitud_seg(list(segmentos))
print("La longitud de los segmentos es:",longitud)