#! /usr/bin/env python3.3
def contarPalabras( cadena ):
	'''devuelve el total de palabras que tienen mas de 5 letras'''
	palabras = cadena.split()
	c = 0
	for palabra in palabras:
		if len(palabra) > 5:
			c += 1
	return c
	
def main():
	cadena = input("Dame texto: ")
	print(contarPalabras(cadena))
	
main()
