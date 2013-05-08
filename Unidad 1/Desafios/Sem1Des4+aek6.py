#!/usr/bin/python
def rombo():
    n = int( input("Dame un numero: ") )

    for j in range( 0, n ):
        print( espacio( n - j ), linea( j+1 ) ) #linea( 0, j+1 )
    for j in range( 1, n ):
        print( espacio( j + 1 ), linea( n-j ) ) #linea( 0, n-j )


def espacio( n ):
    espacio = ""
    for i in range( 0, n ):
        espacio =  espacio + " "
    return espacio

def linea( m ): #( n, m )
    l = ""
    for i in range( 0, m ):
        l =  l + str(i+1) #pintar( n+1, i + 2 )
        
    for i in range( 1, m ):
        l =  l + str(m-i) #pintar( 1, m-i )
        
    return l

'''
def pintar( n, m ):
    p = " "
    for i in range( n, m ):
        p = str(i)
    return p
'''
rombo()
input("(Exit)")
