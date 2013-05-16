#! /usr/bin/env python3.3

def main():
    euros = int( input('Dame los euros: ') )
    billetes_monedas( euros, 0, 0 )

def billetes_monedas( importe, actual, cantidad ):
    '''Desglosa una cantidad de euros en billetes y monedas'''
    for i in ( 500, 200, 100, 50, 20, 10, 5, 2, 1 ):
        if importe >= i:
            if actual != i:
                if cantidad > 0:
                    print( cantidad, billeteMoneda( actual, cantidad ), 'de', actual, 'euro' + esUno( actual ) )
                actual = i
                cantidad = 0
            llamalo( importe - i, actual, cantidad + 1 )
            return 0
    print( cantidad, billeteMoneda( actual, cantidad ), 'de', actual, 'euro' + esUno( actual ) )

def llamalo( importe, actual, cantidad ):
    billetes_monedas( importe, actual, cantidad )

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

