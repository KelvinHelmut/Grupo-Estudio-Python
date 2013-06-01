#! /usr/bin/env python3.3
def procesarTelegrama( texto, longitudMax, costoCorta, costoLarga ):
	lTexto = texto.split()
	costo = 0
	puntos = 0
	for i in range(len(lTexto)):
		i += puntos
		print( lTexto[i] )
		if lTexto[i][len(lTexto[i])-1] == '.':
			lTexto[i] = lTexto[i][0:len(lTexto[i])-2]
			lTexto.insert( i + 1, 'STOP')
			puntos += 1
		if len(lTexto[i]) > longitudMax:
			lTexto[i] = lTexto[i][:longitudMax] + '@'
			costo += costoLarga
		else:
			costo += costoCorta
	if lTexto[len(lTexto)-1] == 'STOP':
		lTexto[len(lTexto)-1] += 'STOP'
	else:
		lTexto.append('STOPSTOP')
	return " ".join(lTexto), costo
	
def main():
	print('Procesador de telegramas')
	texto = input('Dame texto: ')
	longmax = int(input('longituda maxima de las palabras:'))
	corta = float(input('costo de palabra corta: '))
	larga = float(input('costo de palabra larga: '))
	texto, costo = procesarTelegrama( texto, longmax, corta, larga )
	print(texto)
	print('Costo:', costo)
	
main()
