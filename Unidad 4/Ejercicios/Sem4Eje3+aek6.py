#! /usr/bin/env python3.3

def main():
    actualidad = int( input('¿En que año estamos?: ') )
    cualquiera = int( input('Dame un año cualquiera: ') )

    diferencia = actualidad - cualquiera

    if diferencia == 0:
        print('¡Son el mismo año!')
    elif diferencia > 0:
        print('Desde el año', cualquiera, 'ha passado', diferencia, anios(diferencia) )
    else:
        print('Para llegar al año', cualquiera, 'falta', diferencia * -1, anios(diferencia * -1) )

def anios( anios ):
    if anios == 1:
        return 'año'
    return 'años'

main()
