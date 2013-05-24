#! /usr/bin/env python3.3
def interactivo():
	'''Pedir numero positivo en bucle interactivo'''
	continuar = 'si'
	while continuar == 'si':
		t = input("numero positivo: ")
		if esPositivo(t):
			continuar = 'no'
		else:
			print("El valor:", '"' + t + '"', "No es un numero positivo.")
			continuar = input("¿continuar pidiendo el numero? [si/no]: ")
		print("")

def centinela():
	'''Pedir numero positivo en bucle centinela'''
	n = -1
	while n < 0:
		t = input("numero positivo: ")
		if esPositivo(t):
			n = 1
		else:
			n = -1
			print("El valor:", '"' + t + '"', "No es un numero positivo.")
		print("")
		
def infinito():
	'''Pedir numero positivo en bucle infinito'''
	while True:
		t = input("numero positivo: ")
		if esPositivo(t):
			break
		else:
			n = -1
			print("El valor:", '"' + t + '"', "No es un numero positivo.")
		print("")

def esPositivo( texto ):
	punto = 0
	for e in texto:
		if not esNumero(e):
			if e == '.' and punto == 0:#si solo tiene un punto es numero
				punto += 1
			else:
				return False
	return True
	
def esNumero( e ):
	for n in ('0','1','2','3','4','5','6','7','8','9'):
		if e == n:
			return True
	return False

	
def main():
	#interactivo()
	#centinela()
	infinito()
	
main()
