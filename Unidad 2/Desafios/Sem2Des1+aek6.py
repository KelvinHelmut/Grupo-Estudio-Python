#! /usr/bin/env python3.3

#obtener numero decimal a partir de un numero binario
def getDecimal( binario ):
    contador = 0
    acumulador = 0

    #invertimos el binario: 110 -> 011
    binarioInvertido = ""
    for i in binario:
        binarioInvertido = i + binarioInvertido
        
    #trabajamos con el binario invertido
    for i in binarioInvertido:
        acumulador += ( int(i) * ( 2 ** contador ) )
        contador += 1
    return acumulador

def convertirBinarioADecimal():
    binario = input("Dame un binario: ");
    #llmamos a la funcion que nos devuelve el numero en sistema decimal
    print( getDecimal(binario) )

convertirBinarioADecimal();
