#! /usr/bin/env python3.3

import math

def main():
    print('Hallar el valor de x -> ax² + b x + c = 0')
    a = float( input('Dame valor para a: ') )
    b = float( input('Dame valor para b: ') )
    c = float( input('Dame valor para c: ') )
    
    if a == 0:
        if b == 0 and c == 0:
            print('Todos los numeros son solucion')
        else:
            print('Sin solucion')
    else:
        d = b**2 - 4*a*c
        if d < 0:
            print('Sin solucion real')
        else:
            x1 = ( -b + math.sqrt( d ) ) / ( 2 * a )
            x2 = ( -b - math.sqrt( d ) ) / ( 2 * a )
            if d == 0:
                print('Una Solucion:', x1 )
            else:
                print('Las soluciones de la ecuacion son:', x1, 'y', x2 )

main()
