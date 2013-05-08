#!/usr/bin/python3.3

def sumarDigitos( numero ):
    '''Suma los digitos de el numero ingresado'''
    suma = 0
    for i in numero:
        suma += int(i)
    return suma
    

numero = input( 'Dame un numero:' )
print( sumarDigitos( numero ) )
