#!  /usr/bin/env python3.3

def main():
    lista = input('Dame una lista ( separada por comas ","; sin espacios ): ')
    print( '[ ' + ordenarLista( lista, 0 ) + ' ]')

def ordenarLista( lista, indice ):
    elemento = ''
    t = tamanioLista( lista )
    
    if indice < t - 1: #mejor un while
        e1 = getElementoLista( lista, indice )
        e2 = getElementoLista( lista, indice + 1 )

        o1 = ''
        o2 = ''
        x = 0
        #if para inicio x
        if ( getElemento( 0, e1 ) == 'x' or getElemento( 0, e1 ) == 'X' ) and  not( getElemento( 0, e2 ) == 'x' or getElemento( 0, e2 ) == 'X' ):
            o1 = e1
            o2 = e2
        elif not( getElemento( 0, e1 ) == 'x' or getElemento( 0, e1 ) == 'X' ) and ( getElemento( 0, e2 ) == 'x' or getElemento( 0, e2 ) == 'X' ):
            o1 = e2
            o2 = e1
        else:
            o1, o2 = ordena( e1, e2 )
        
        if  e1 != o1:
            lista = sobreEscribirLista( lista, indice, o1, o2 )
            if indice > 0:
                indice -= 1
        else:
            indice += 1

        lista = ordenarLista( lista, indice )
    
    return lista

#equivalente a miLista[indice]
def getElementoLista( lista, indice ):
    '''me retorna el elemento con indice x de mi lista'''
    c = 0
    elemento = ''
    for i in lista:
        if i == ',':
            if c == indice:
                return elemento
            elemento = ''
            c += 1
        else:
            elemento += i
            
    if c == indice:
        return elemento
    return ''

#equivalente a len(miLista)
def tamanioLista( lista ):
    '''retorna el tamaño de mi lista'''
    c = 0
    for i in lista:
        if i == ',':
            c += 1
    return c + 1

def ordena( elemento, comparacion ):
    '''cordena a lo parametros por orden alfabetico'''
    if  elemento == '':
        elemento = ' '
    if comparacion == '':
        comparacion = ' '
        
    te = len(elemento)
    tc = len(comparacion)
    t = 0
    if te < tc:
        t = tc
    else:
        t = te
        
    for i in range(t):
        e1 = getElemento( i, elemento )
        e2 = getElemento( i, comparacion )
        if e1 > e2:
            return ( comparacion, elemento )
        elif e1 < e2:
            return ( elemento, comparacion )
        
    return ( elemento, comparacion )

def getElemento( indice, lista ):
    '''retorna el indice de una lista'''
    c = 0
    for i in lista:
        if c == indice:
            return i
        c += 1
    return ''

def sobreEscribirLista( lista, indice, e1, e2 ):
    c = 0
    nuevaLista = ''
    elemento = ''
    for i in lista:
        if i == ',':
            if c == indice:
                nuevaLista += coma(nuevaLista) + e1
            elif c == indice + 1:
                nuevaLista += coma(nuevaLista) + e2
            else:
                nuevaLista += coma(nuevaLista) + elemento
            elemento = ''
            c += 1
        else:
            elemento += i

    if c == indice:
        nuevaLista += coma(nuevaLista) + e1
    elif c == indice + 1:
        nuevaLista += coma(nuevaLista) + e2
    else:
        nuevaLista += coma(nuevaLista) + elemento
                
    return nuevaLista

def coma( lista ):
    '''si lista no esta vacia devuelve ","'''
    for i in lista:
        return ','
    return ''

main()
