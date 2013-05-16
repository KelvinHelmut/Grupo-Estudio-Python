#! /usr/bin/env python3.3

def main():
    a = int( input('Dame un numero: ') )
    b = int( input('Dame otro numero: ') )

    if a > b:
        esMultiplo( a, b )
    else:
        esMultiplo( b, a )


def esMultiplo( my, mn ):
    '''Verifica si my es multiplo de mn'''
    if my % mn == 0:
        print( my,'es multiplo de', mn )
    else:
        print( my,'no es multiplo de', mn )


main()
