#! /usr/bin/env python3.3
def invertirTexto( cadena ):
	''' retorna la cadena dada de fin a incio'''
	nuevo = ""
	for c in range( 1, len(cadena) + 1 ):
		nuevo += cadena[ c * -1 ]
	return nuevo
	
print( invertirTexto( input("Dame un texto: ") ) )
