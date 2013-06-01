#! /usr/bin/env python3.3
def sumaTiempos( tiempos ):
	'''suma tiempos representados en tuplas'''
	suma = 0
	for tiempo in tiempos:
		suma += aSegundos( tiempo )
	return aTiempo( suma )
			
def aSegundos( tiempo ):
	'''convierte un tiempo representado en una tupla a segundos'''
	return tiempo[0] * 3600 + tiempo[1] * 60 + tiempo[2]
	
def aTiempo( segundos ):
	'''devuelve los segundos convertidos a h,m,s en una tupla'''
	return int(segundos/3600), int(( segundos%3600 )/60), segundos%60
	
def main():
	tiempos = ( (2,23,0), (1,56,48), (0,8,12) )
	print( sumaTiempos(tiempos) )
	
main()
