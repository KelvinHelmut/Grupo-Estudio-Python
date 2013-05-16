#! /usr/bin/env python3.3

import math

def main():
    op = input('Calcular el area de [ Triangulo / Circulo ]: ')
    if op == 'T' or op == 't':
        b = float( input('Dame la base: ') )
        h = float( input('Dame la altura: ') )
        print('Un triangulo de base:', b, 'y altura:', h, 'tiene un area de', b * h / 2)
    elif op == 'C' or op == 'c':
        r = float( input('Dame el radio: ') )
        print('Un circulo de radio:', r, 'tiene un area de:', math.pi * r**2 )
    else:
        print('Digite C o T para ejecutar la aplicacion.')
        main()

main()
