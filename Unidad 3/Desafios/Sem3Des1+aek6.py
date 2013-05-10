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


numero = int( input( 'Dame al que se cree primo: ' ) )
print ( esPrimo( numero ) )
