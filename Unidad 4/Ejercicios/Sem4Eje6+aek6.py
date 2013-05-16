#! /usr/bin/env python3.3

def main():
    anio = int( input('Escriba un año y le dire si es bisiesto: ') )
    esBisiesto( anio )

def esBisiesto( anio ):
    if anio % 400 == 0:
        print('El año', anio, 'es un año bisiesto porque es multiplo de 400.')
        return 0
    elif anio % 100 == 0:
        print('El año', anio, 'no es un año bisiesto')
        return 0
    elif anio % 4 == 0:
        print('El año', anio, 'es un año bisiesto porque es multiplo de 4.')
        return 0
    else:
        print('El año', anio, 'no es un año bisiesto')
    return 0

main()
