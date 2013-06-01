#! /usr/bin/env python3.3
def AvsE( cadena ):
	'''Decide que letra hay mas veces entre A y E'''
	a = 0
	e = 0
	for ch in cadena:
		if ch == 'a' or ch == 'A':
			a += 1
		elif ch == 'e' or ch == 'E':
			e += 1
	if a > e:
		print('Hay mas letras "A" que "E"')
	elif a < e:
		print('Hay mas letras "E" que "A"')
	else:
		print('Hay igual de letras "A" que "E"')
		
AvsE( input("Dame texto: ") )
