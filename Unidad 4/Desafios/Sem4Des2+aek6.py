#! /usr/bin/env python3.3

def main():
    lista = input('Dame lista ( separada por comas ","; sin espacios C: ): ')
    elemento = ''
    contador = 0
    for i in lista:
        if i == ',':
            if esElBuscado( elemento ):
                contador += 1
            elemento = ''
        else:
            elemento += i
    if esElBuscado( elemento ):
        contador += 1
    print( contador )

def esElBuscado( elemento ):
    '''retorna 1 si la longitud de "e" es mayor 2
    y sus primer y ultimo caracter son iguales'''
    c = 0
    p = ''
    f = ''
    if len(elemento) >= 2:
        for i in elemento:
            if c == 0:
                p = i
            f = i
            c += 1
        if p == f:
            return True
    return False

main()
