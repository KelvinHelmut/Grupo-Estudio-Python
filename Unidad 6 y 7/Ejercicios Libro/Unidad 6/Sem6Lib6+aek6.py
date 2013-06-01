#! /usr/bin/env python3.3
def cuentaVocales( cadena ):
	'''cuenta las veces que aprarece cada vocal en la cadena '''
	a,e,i,o,u = 0,0,0,0,0
	for c in cadena:
		if c == 'a' or c == 'A':
			a += 1
		elif c == 'e' or c == 'E':
			e += 1
		elif c == 'i' or c == 'I':
			i += 1
		elif c == 'o' or c == 'O':
			o += 1
		elif c == 'u' or c == 'U':
			u += 1
	return a,e,i,o,u
	
a,e,i,o,u = cuentaVocales( input("Dame texto: ") )
print("Veces que aparecen las vocales:", "a =", a, ", e =", e, ", i =", i, ", o =", o, ", u =", u )
