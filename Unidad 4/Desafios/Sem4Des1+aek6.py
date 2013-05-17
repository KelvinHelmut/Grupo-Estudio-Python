#! /usr/bin/env python3.3

def main():
    lista = input("Dame lista ( separada por ','; sin espacios C: ): ")
    elemento = ''
    nuevaLista = ''
    for i in lista:
        if i == ',':
            if not( existeElemento( elemento, nuevaLista ) ):
                nuevaLista += coma(nuevaLista) + elemento
            elemento = ''
        else:
            elemento += i
            
    if not( existeElemento( elemento, nuevaLista ) ):
        nuevaLista += coma(nuevaLista) + elemento
        
    print( '[' + nuevaLista + ']' )

def existeElemento( e, lista ):
    '''verifica si existe e en lista'''
    elemento = ''
    for i in lista:
        if i == ',':
            if e == elemento:
                return True
            elemento = ''
        else:
            elemento += i
            
    if e == elemento:
        return True
    
    return False

def coma( lista ):
    '''si lista no esta vacia devuelve ","'''
    for i in lista:
        return ','
    return ''

main()
