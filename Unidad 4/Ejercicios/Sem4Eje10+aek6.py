#! /usr/bin/env python3.3

def main():
    d = int( input('Dame la distancia en centimetros: ') )

    km = obtenerUnidad( d, 100000 )
    m = obtenerUnidad( d % 100000, 100 )
    cm = d % 100

    s = separadores( ( m, cm ) )

    cadena = ''
    if mostrar(km):
        cadena = str(km) +'km' + separador(s)
    s -= 1
    if mostrar(m):
        cadena += str(m) + 'm' + separador(s)
    if mostrar(cm):
        cadena += str(cm) + 'cm'

    sones = 'son'
    centimetros = 'centimetros '
    if ( km == 1 and m == 0 and cm == 0 ) or ( km == 0 and m == 1 and cm == 0 ):
        sones = 'es'
    if d == 1:
        sones = 'es'
        centimetros = 'centimetro '
        
    print( d, centimetros + sones + ':', cadena + '.' )

def obtenerUnidad( valor, dif ):
    return int( valor / dif )

def separadores( valores ):
    s = 0
    for i in valores:
        if i > 0:
            s += 1
    return s

def separador( separadores ):
    if separadores == 2:
        return ', '
    elif separadores == 1:
        return ' y '
    return ''

def mostrar( valor ):
    if valor > 0:
        return True
    return False

main()
