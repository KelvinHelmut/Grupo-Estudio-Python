#!/usr/bin/python3.3

def esPrimo( n ):
    ''' Verifica si n es primo '''
    for i in range( 2, n ):
        mod = n % i
        for m in range( mod, 1 ):
            return 'No es primo'

    for menores2 in range( n, 2 ):
        return 'No es primo'

    print( n )
    return 'Es primo'


def verificarPrimo():
    numero = int( input( 'Dame al que se cree primo: ' ) )
    print ( esPrimo( numero ) )


def numerosPrimosMenoresA():
    '''numeros primos menores a el numero ingresado
    por el usuario usando la funcion esPrimo()'''
    hasta = int( input( 'Los primos menores a: ' ) )
    for i in range( 0, hasta + 1 ):
        esPrimo( i )
    #primos menores a, usando la criba de esatosteles
    #comentar el for anterior y descomentar lo siguiente
    #primos( hasta )
    

def numerosPrimos():
    cuantos = int( input( 'Cuantos numeros primos quieres ver?: ' ) )
    c = 0
    es = 0
    while es <= cuantos:
        if esPrimo(c) == 'Es primo':
            es += 1
        c += 1



'''criba de esatosteles'''
def primos( n ):
    lNumeros = list( range( 3, n + 1, 2 ) )
    print('cargando...')
    sinfin( lNumeros, n, 0 )
    print('terminado, a imprimir')

    lNumeros = [2] + lNumeros
    for i in lNumeros:
        print( i )

def sinfin( lNumeros, n, i ):
    if( lNumeros[i]**2 < n ):
        #quitarv2( lNumeros[i], lNumeros, i + 1 )
        quitar( lNumeros[i], lNumeros, i + 1 )
        i += 1
        sinfin( lNumeros, n, i )

def quitar( numero, lNumeros, inicio ):
    ''' elimina todos los multiplos de m que hay en la lista primos'''
    eliminados = 0
    t = len( lNumeros )
    for i in range( inicio, t ):
        #if lNumeros[ i - eliminados ] == ( numero * int( lNumeros[i - eliminados ] / numero ) ):
        if lNumeros[i - eliminados ] % numero == 0 :
            del lNumeros[ i - eliminados ]
            eliminados += 1

'''         
def quitarv2( numero, lNumeros, i ):
    if len( lNumeros ) > i:
        if lNumeros[ i ] == ( numero * int( lNumeros[ i ] / numero ) ):
            del lNumeros[ i ]
            quitarv2( numero, lNumeros, i )
        else:
            quitarv2( numero, lNumeros, i+1 )
'''


#Descomentar la funcion a la que se quiere llamar
#numerosPrimos()
#numerosPrimosMenoresA()
#verificarPrimo()
