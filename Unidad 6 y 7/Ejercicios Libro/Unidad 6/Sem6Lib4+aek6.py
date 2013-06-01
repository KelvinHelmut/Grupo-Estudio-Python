#! /usr/bin/env python3.3
def contar( l, x ):
	'''cuenta cuantos caracteres l hay en la cadena x'''
	c = 0
	for ch in x:
		if ch == l:
			c += 1
	return c
	
print( "Aparece: ", contar( input("Carater buscado: "), input("Cadena de texto: ") ) )
