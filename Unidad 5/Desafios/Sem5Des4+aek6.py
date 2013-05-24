#! /usr/bin/env python3.3

#CRIBA DE ESATOSTES
#INICIO CRIBA
def primosMenoresA( n ):
	lNumeros = []
	if n > 2:
		print('Cargando...')
		lNumeros = condicionCriba( n )
	if n >= 2:
		lNumeros = [2] + lNumeros
	print('Listo.')
	return lNumeros

def condicionCriba( n ):
	i = 0
	lNumeros = list( range( 3, n + 1, 2 ) )
	while lNumeros[i]**2 < n:
		print("Eliminado numeros multiplos de:", lNumeros[i], "...")
		quitar( lNumeros[i], lNumeros, i + 1 )
		i += 1
	return lNumeros

def quitar( numero, lNumeros, inicio ):
    ''' elimina todos los multiplos de m que hay en la lista primos'''
    eliminados = 0
    t = len( lNumeros )
    for i in range( inicio, t ):
        if lNumeros[i - eliminados ] % numero == 0 :
            del lNumeros[ i - eliminados ]
            eliminados += 1
#FIN CRIBA


def esPrimo(n):
	'''Verifica si n es primo'''
	if n % 2 == 0 or n < 2:
		return False
	for i in range( 3, n, 2 ):
		if n % i == 0:
			return False
	return n
	
def nPrimosMenoresA( n ):
	if n >= 2:
		print(2)
	for i in range( 3, n+1, 2 ):
		if esPrimo( i ) != False:
			print(i)

def sumaPrimos( primos, n ):
	lista = []
	p2 = 2
	p3 = 3
	t = len(primos)
	f1 = t #tendra el indice del primo mayor encontrado en ciclo 2
	f2 = t #tendra el indice del primo mayor encontrado en ciclo 3
	bf1 = False #true si f2 recibe valor primera vez en el ciclo
	for	i in range( 1, t ):
		for j in range( p2, t ):
			for k in range( p3, f2 ):
				if ( primos[i] + primos[j] + primos[f2 - k + p3 - 1] ) == n:
					#lista.append( str(primos[i]) + "+" + str(primos[j]) + "+" + str(primos[f2 - k + p3 - 1]) + " = " + str(n) )
					print( str(primos[i]) + "+" + str(primos[j]) + "+" + str(primos[f2 - k + p3 - 1]) + " = " + str(n) )
					f2 = f2 - k + p3 - 1
					if not bf1:
						f1 = f2
						bf1 = True
						#return 0 #para terminar cuando encuentre tres numeros sumado = a n
					p3 += 1
					break
				elif ( primos[i] + primos[j] + primos[f2 - k + p3 - 1] ) < n:
					p3 += 1
					break
					
		p2 += 1
		p3 = p2 + 1
		f2 = f1
		bf1 = False
	#return lista
        
def main():
	numero = int(input("Dame numero entero impar mayor que 5: "))
	if numero % 2 == 1 and numero > 5:
		#usando criba de esatosteles - uso de listas
		print("-------------------------------------")
		print("Primos")
		l = primosMenoresA( numero )
		print(l)
		
		print("-------------------------------------")
		print("Lista de primos sumados  daran",numero)
		print("cargando...")
		sumaPrimos( l, numero )
		
		#sin uso de listas mas lento mucho mas lento
		#nPrimosMenoresA( numero )
	else:
		main()

main()
