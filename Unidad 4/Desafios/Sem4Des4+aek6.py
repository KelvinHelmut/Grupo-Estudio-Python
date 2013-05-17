#! /usr/bin/env python3.3

def main():
    euros = int( input('Dame los euros: ') )
    desglosa( euros )

def desglosa( importe ):
    '''Desglosa una cantidad de euros en billetes y monedas'''
    b = base( importe )
    c = int( importe / b )
    print( c, billeteMoneda( b, c ), 'de', b, 'euro' + esUno( b ) )
    if importe % b > 0:
        desglosa( importe % b )
        
def base( importe ):
    '''retorna la base de billete o moneda'''
    for i in ( 500, 200, 100, 50, 20, 10, 5, 2, 1 ):
        if importe >= i:
            return i
    return importe

def billeteMoneda( valor, c ):
    '''retorna la cadena billete(s) o moneda(s)'''
    if esBillete( valor ):
        return 'billete' + esUno( c )
    return 'moneda' + esUno( c )

def esBillete( valor ):
    '''Determina si sera billete o moneda'''
    if valor <= 5:
        return False
    return True
    
def esUno( valor ):
    ''' si el valor es mas de 1 devulve s para hacer plural'''
    if valor == 1:
        return ''
    return 's'


main()
