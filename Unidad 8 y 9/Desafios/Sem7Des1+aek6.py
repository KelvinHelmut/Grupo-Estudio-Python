#! /usr/bin/env python3.3
def getCode():
    '''Pide codigo al usuario y lo devuelve
	en un diccionario'''
    code = {}
    n = 0
    while True:
        n += 1
        code[n] = input( str(n) + '\t')
        if len(code[n]) == 0 or emptyText( code[n] ):
            code[n] += ' '
        if code[n].lower() == 'exit':
            code.pop(n)
            break
    return code
    
def emptyText( texto ):
    '''verifica si el texto es vacio, si no tiene caracteres'''
    for c in texto:
        if c != '\t' and c != ' ':
            return False
    return True
    
def testCode( code ):
    '''verifica si tiene errores de identacion'''
    iden = 0
    block = False
    for i in code:
        if emptyText( code[i] ):
            continue
        for n in range(iden+1):
            if code[i][0 + n] == '\t':
                if n == iden:
                    printError(i)
            elif code[i][0 + n] == ' ':
                printError(i)
                block = False
                break
            else:
                if block:
                    if n < iden:
                        printError( i )
                block = False
                iden = n
                break
        if code[i][-1] == ':':
            block = True
            iden += 1
    
def printError( linea ):
    '''imprime el mensaje de error de identacion'''
    print('Error!: En la linea', linea)
    
def main():
    testCode( getCode() )
    
main()
