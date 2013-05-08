#!/usr/bin/python3.3

def tabla( tabla, inicio, fin ):
    '''muestra la tabla de multiplicacion del numero 'tabla' desde 'inicio' hata 'fin' '''
    for i in range( inicio, fin ):
        print( tabla, 'x', i, '=', tabla * i )

        
hasta = int( input( '¿Hasta que tabla debemos imprimir?: ' ) )
inicio = int( input( '¿En donde debe iniciar la tabla?: ' ) )
fin = int( input( '¿En donde debe terminar la tabla?: ' ) )
for i in range( 0, hasta ):
    print('')
    tabla( i + 1, inicio, fin + 1 )


