#! /usr/bin/env python3.3

def main():
    a = input('Dame un numero: ')
    b = input('Dame otro numero: ')
    c = input('Dame otro numero mas: ')

    if a == b or a == c or b == c:
        if a == b and a == c:
            print('Ha escrito tres veces el mismo numero')
        else:
            print('Ha escrito uno de los numeros dos veces')
    else:
        print('los tres numeros que ha escrito son distintos')

main()
