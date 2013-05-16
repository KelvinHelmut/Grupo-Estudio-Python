#! /usr/bin/env python3.3

def main():
    '''El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo.'''

    mx = int( input( 'Duracion maxima de una llamada corta <en segundos>: ' ) )
    tc = float( input( 'Tarifa llamadas cortas por segundo: ' ) )
    ta = float( input( 'Tarifa llamadas largas por segundo: ' ) )
    c = int( input( 'Comunicaciones realizadas: ' ) )

    total = 0
    
    for i in range( c ):
        h = int( input( '¿Cuantas horas?: ' ) )
        m = int( input( '¿Cuantos minutos?: ' ) )
        s = int( input( '¿Cuantos segundos?: ' ) )

        tiempo = aSegundos( h, m, s )
        costo = 0
        if tiempo <= mx:
            costo = tiempo * tc
        else:
            costo = tiempo * ta
            
        pesos, centavos = moneda( costo )

        total += costo
        
        print( 'Duracion:', tiempo, 'segundos. Costo:', pesos, 'pesos y', centavos, 'centavos' )

    pesos, centavos = moneda( total )
    print( 'Total facturado:', pesos, 'pesos y', centavos, 'centavos' )

def aSegundos( h, m, s ):
    return 3600 * h + 60 * m + s

def moneda( importe ):
    return( int(importe), importe%int(importe) * 10 )

main()
