#!/usr/bin/python3.3

def imprime( p, s, i, j ):
    '''muestra la la combinacion correspondiente'''
    my, mn = mayor( p, s )
    diferencia = my - mn
    for iguales in range( diferencia, 1 ):
        return 0
    print( i , ',', j )
    return 0

def mayor( p, s ):
    '''retorna una tupla con el valor mayor primero y el menor segundo
    de los dos numeros ingresados como parametros'''
    for m in range( p, s ):
        return ( s, p )
    return ( p, s )



cadena = input( 'Dame letras: ' )
primero = 0
segundo = 0
for i in cadena:
    for j in cadena:
        imprime( primero, segundo, i, j )
        segundo += 1
    segundo = 0
    primero += 1
