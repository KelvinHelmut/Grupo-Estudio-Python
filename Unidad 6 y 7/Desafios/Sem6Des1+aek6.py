#! /usr/bin/env python3.3
#la version alpha, falta ver que se puede mejorar
def creaDisenio():
	'''Permite crear diseños a partir de patrones
	y desplazamientos'''
	capas = int(input("¿Cuantas capas tendra el diseño?: "))
	ancho = int(input("¿Cual sera el ancho del patron?: "))
	serie = ""
	for i in range(ancho):
		serie += str((i+1)%10)
	disenio = []
	despla = []
	posicion = []
	for i in range( capas ):
		print("Introdusca el diseño de la capa", i,":")
		print(serie)
		print("|", " " * (ancho - 4), "|")
		disenio.append(input(""))
		despla.append(input("¿Cual sera el desplazamiento de esta capa (-1, 0, 1)?: "))
		print("")
		posicion.append(0)
	hiladas = int(input("¿Cuantas hiladas tendra el diseño?: "))
	
	for i in range(hiladas):
		linea = ((" ," * (ancho - 1)) + " ").split(",")
		for l in range(capas):		
			for c in range(ancho):
				if disenio[l][c] != " ":
					linea[c+posicion[l]-ancho] = disenio[l][c]
			posicion[l] += int(despla[l])
			if posicion[l] == ancho:
				posicion[l] = 0;
			if posicion[l] == -1:
				posicion[l] = ancho -1;
		print("".join(linea))
	
					
creaDisenio()
