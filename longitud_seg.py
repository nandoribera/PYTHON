#usr/bin/env python3

#Función longitud variable de segmentos
def longitud_seg(*segmentos):
	suma = 0
	for segmento in segmentos:
		suma = segmento + suma
	return suma

#Paso de parámetros de forma manual
longitud = longitud_seg(2,4,-3,5)
print("La longitud de los segmentos es:",longitud)