#!/usr/bin/python3.3

def factorial( n ):
    '''Retorna el factorial del numero ingresado'''
    factorial = 1;
    for i in range( 0, n ):
        factorial *= ( i + 1 )
        
    return factorial
        

numero = int( input( 'Dame el numero: ' ) )
print( factorial( numero ) )
