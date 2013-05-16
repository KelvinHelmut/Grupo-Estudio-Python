#! /usr/bin/env python3.3

def main():
    a = float( input('Dame valor: ') )
    b = float( input('Dame valor: ') )

    if a == b:
        print('Los dos números son iguales')
    elif a > b:
        print('Mayor:',a,'Menor:',b)
    else:
        print('Mayor:',b,'Menor:',a)

main()
