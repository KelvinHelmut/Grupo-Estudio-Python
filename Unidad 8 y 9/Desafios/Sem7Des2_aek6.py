#! /usr/bin/env python3.3
# -*- coding: utf-8 -*-

def agregar( lista, n ):
    datos = {}
    datos['nombre'] = ''
    datos['apellido'] = ''
    while len(datos['nombre']) < 1:
        datos['nombre'] = input('Nombre: ')
    while len(datos['apellido']) < 1:
        datos['apellido'] = input('Apellido: ')
    datos['edad'] = input('Edad: ')
    datos['telefono'] = input('Teléfono: ')
    datos['email'] = input('Correo Electrónico: ')
    datos['localidad'] = input('Localidad: ')
    lista[str(n)] = datos
        
def eliminar( lista, n ):
    if n in lista:
        lista.pop(n)
        
def editar( lista, n ):
    if n in lista:
        for e in lista[n]:
            lista[n][e] = input(e + ' ' + lista[n][e] + ': ')

def informe( lista ):
    n = 0
    opciones = []
    vistas = []
    for e in lista:
        for campo in lista[e]:
            n += 1
            print(n,campo)
            opciones.append(campo)
        break
    if n == 0:
        print('La lista esta vacia.')
        return 0
    op = input('Ingrese el o los numeros de los campos que quiere ver(dejando un espacio entre ellos): ')
    for ops in op.split():
        vistas.append(opciones[int(ops)-1])
    for e in lista:
        fila = ''
        for v in vistas:
            fila += lista[e][v] + ' '
        print(fila)
    
def main():
    participantes = {}
    i = 0
    print('Participantes de Curso')
    while True:
        print('1. Agregar\n2. Editar\n3. Eliminar\n4. Informe\n5. Salir')
        op = input('Ingrese Opcion: ')
        if op not in ('1','2','3','4','5'):
            print('Opcion invalida.\n')
            continue
        if op == '1':
            i += 1
            agregar( participantes, i )
        elif op == '2':
            for e in participantes:
                print(e, participantes[e]['nombre'], participantes[e]['apellido'] )
            n = input('Ingrese número del participante a eliminar: ')
            editar( participantes, n )
        elif op == '3':
            for e in participantes:
                print(e, participantes[e]['nombre'], participantes[e]['apellido'] )
            n = input('Ingrese número del participante a eliminar: ')
            eliminar( participantes, n )
        elif op == '4':
            informe( participantes )
        elif op == '5':
            break
main()
