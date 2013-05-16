#! /urs/bin/env python3.3

def main():
    print('Hallar el valor de x -> ax + b = 0')
    a = float( input('Dame el valor de a: ') )
    b = float( input('Dame el valor de b: ') )

    if a == 0:
        if b == 0:
            print('todos los numeros son solucion')
        else:
            print('Sin solucion, para que tenga solucion a no tiene que ser 0')
    else:
        print('La solucion de la ecuacion es:', -b/a )
        
main()
    
