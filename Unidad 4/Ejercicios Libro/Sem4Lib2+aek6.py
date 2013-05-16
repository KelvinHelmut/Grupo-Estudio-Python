#! /usr/bin/env python3.3

def main():
    '''El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo.'''

    mx = int( input( 'Duracion maxima de una llamada corta <en segundos>: ' ) )
    tc = float( input( 'Tarifa llamadas cortas por segundo pesos: ' ) )
    ta = float( input( 'Tarifa llamadas largas por segundo: ' ) )
    c = int( input( 'Comunicaciones realizadas: ' ) )

    totalCortas = 0
    totalLargas = 0
    cortas = 0
    largas = 0
    
    for i in range( c ):
        h = int( input( '¿Cuantas horas?: ' ) )
        m = int( input( '¿Cuantos minutos?: ' ) )
        s = int( input( '¿Cuantos segundos?: ' ) )

        tiempo = aSegundos( h, m, s )
        costo = 0
        if tiempo <= mx:
            costo = getCosto( tiempo, tc )
            totalCortas += costo
            cortas += 1
        else:
            costo = getCosto( tiempo, ta )
            totalLargas += costo
            largas += 1
            
        pesos, centavos = moneda( costo )        
        print( 'Duracion:', tiempo, 'segundos. Costo:', pesos, 'pesos y', centavos, 'centavos' )

    
    print( 'Cantidad de llamadas cortas:', cortas )
    pesos, centavos = moneda( totalCortas )
    print( 'Total llamadas cortas:', pesos, 'pesos y', centavos, 'centavos' )
    print( 'Cantidad de llamadas largas:', largas )
    pesos, centavos = moneda( totalLargas )
    print( 'Total llamadas largas:', pesos, 'pesos y', centavos, 'centavos' )
    pesos, centavos = moneda( totalLargas + totalCortas )
    print( 'Total facturado:', pesos, 'pesos y', centavos, 'centavos' )

def getCosto( duracion, tarifa ):
    return duracion * tarifa

def aSegundos( h, m, s ):
    return 3600 * h + 60 * m + s

def moneda( importe ):
    return( int(importe), importe%int(importe) * 10 )

main()
