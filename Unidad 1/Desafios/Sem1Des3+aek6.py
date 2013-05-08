#!/usr/bin/python
def barras():
    m = int( input("Tamanho maximo: ") )
    t1 = int( input("Tamanho de barra1: ") )
    t2 = int( input("Tamanho de barra2: ") )
    t3 = int( input("Tamanho de barra3: ") )
    t4 = int( input("Tamanho de barra4: ") )
    print("")
    print("El maximo alcance de la barra es: ", m )
    print("+++++++++++++++++++++++")
    for i in range( 0, m ):
        print( "+", barra( t1, m - i ), barra( t2, m - i ), barra( t3, m - i ), barra( t4, m - i ), "+" )
    
    print("+  b1 "," b2 "," b3 "," b4  +")
    print("+++++++++++++++++++++++")
    input("(Exit)")

def barra( t, m ):
    b = "    "
    for i in range( t, m ):
        b = "____"

    return b

barras()
