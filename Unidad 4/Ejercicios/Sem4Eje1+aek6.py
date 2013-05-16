#! /usr/bin/env python3.3

def main():
    dividendo = int( input( 'Dame dividendo: ' ) )
    divisor = int( input( 'Dame divisor: ' ) )
    if divisor == 0:
        print('No se puede dividir por 0')
    else:
        cociente = int( dividendo / divisor )
        resto = dividendo % divisor
        if resto > 0:
            print('La division no es exacta. Cociente:', cociente, 'Resto:', resto)
        else:
            print('La division es exacta. Cociente:', cociente)

main()
