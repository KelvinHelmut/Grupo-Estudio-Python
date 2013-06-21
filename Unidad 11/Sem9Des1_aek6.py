# /usr/bin/env python3.3
# -*- coding: utf-8 -*-
import csv
import os

campos = ('ID','Nombre','Teléfono','E-mail')

def main():
    archivo = 'agenda.csv'
    while True:
        print('AGENDA DE CONTACTOS')
        opcion = input('[N]Nuevo\n[E]Editar\n[R]Remover\n[L]Listar\n[B]Buscar\n[S]Salir\n\nIngrese una opcion: ')
        if opcion.lower() == 'n':
            nuevo( archivo )
        elif opcion.lower() == 'e':
            ID = input('Identificador del registro: ')
            datos = [ID] + list(obtenerDatos('Nuevo '))
            editar( archivo, datos )
        elif opcion.lower() == 'r':
            ID = input('Identificador del registro: ')
            remover( archivo, ID )
        elif opcion.lower() == 'l':
            listar(archivo)
        elif opcion.lower() == 'b':
            print('Buscar Por:')
            op = input('[1]' + campos[1] + '  [2]' + campos[2] + '  [3]' + campos[3] + ": ")
            if op == '1' or op == '2' or op == '3':
                ocurrencia = input('Buscar: ')
                buscar(ocurrencia, int(op), archivo)
        elif opcion.lower() == 's':
            break
        limpiar()
    
def escribir( escritor, fila ):
    '''agrega nueva linea al archivo'''
    escritor.writerow(fila)
    
def remover( nombreArchivo, codigo ):
    '''elimina una linea del archivo'''
    archivo = abrirArchivo( nombreArchivo, False )
    lector = list(csv.reader(archivo))
    archivo.close()
    archivo = abrirArchivo( nombreArchivo, True )
    escritor = csv.writer(archivo)
    for linea in lector:
        if linea[0] == codigo:
            print('El registro:')
            imprimir( [linea] )
            print('Fue removido.')
            input('Continuar.')
        else:
            escribir( escritor, linea )
    archivo.close()

def editar( nombreArchivo, fila ):
    '''cambia una linea del archivo por otra'''
    archivo = abrirArchivo( nombreArchivo, False )
    lector = list(csv.reader(archivo))
    archivo.close()
    archivo = abrirArchivo( nombreArchivo, True )
    escritor = csv.writer(archivo)
    for linea in lector:
        if linea[0] == fila[0]:
            escribir(escritor, fila)
            print('El registro:')
            imprimir([linea])
            print('Fue cambiado por:')
            imprimir([fila])
            input('Continuar.')
        else:
            escribir( escritor, linea )
    archivo.close()
    
def listar( nombreArchivo ):
    '''lista los datos del archivo'''
    archivo = abrirArchivo( nombreArchivo, False )
    lector = csv.reader(archivo)
    imprimir(list(lector))
    archivo.close()
    input('Continuar.')
    
def buscar( texto, i, nombreArchivo ):
    '''busca un texto en el archivo'''
    archivo = abrirArchivo( nombreArchivo, False )
    lector = csv.reader(archivo)
    encontrados = []
    for linea in lector:
        if texto.lower() in linea[i].lower():
            encontrados.append(linea)
    if len(encontrados) > 0:
        imprimir(encontrados)
    else:
        print('No hay coincidencias con el valor buscado.')
    archivo.close()
    input('Continuar.')

def nuevo( nombreArchivo ):
    '''registra una nueva fila en el archivo'''
    nombre, telefono, email = obtenerDatos('')
    
    archivo = abrirArchivo( nombreArchivo, False )
    lector = csv.reader(archivo)
    escritor = csv.writer(archivo)
    ID = nuevoId(lector)
    archivo.readline()
    escribir( escritor, [ID, nombre, telefono, email] )
    archivo.close()
    
def obtenerDatos( nuevo ):
    nombre = input(nuevo + campos[1] + ': ')
    telefono = input(nuevo + campos[2] + ': ')
    email = input(nuevo + campos[3] + ': ')
    return nombre, telefono, email
    
def nuevoId( datos ):
    '''generar nuevo id para el nuevo registro'''
    data = list(datos)
    print(data)
    if len(data) > 0:
        return (1 + int(data[len(data)-1][0]))
    return 1
    
def abrirArchivo( nombreArchivo, nuevo ):
    '''abrir un archivo
    si no existe o si nuevo = True crearlo
    y si existe y nuevo = False abrirlo en modo lectura-escritura'''
    if not os.path.exists(nombreArchivo) or nuevo:
        return open(nombreArchivo, "w+")
    elif os.path.isfile(nombreArchivo):
        return open(nombreArchivo, "r+")
    else:
        print("Error, %s no es un archivo" %nombreArchivo)
    return None
    
def limpiar():
    '''Limpiar pantalla'''
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("<-No se pudo borrar la pantalla->")
        
def imprimir( filas ):
    '''imprime tabla de datos'''
    filas.insert(0,campos)
    longis = preparaTabla(filas)
    for fila in filas:
        texto = '|'
        marco = '+'
        for i in range(len(fila)):
            longi = longis[i] + 2
            marco += ('-' * longi ) + '+'
            texto += ' ' + str(fila[i]) + (' ' * (longi - len(fila[i]) - 1) ) + '|'
        if fila == campos:
            print(marco)
        print(texto)
        print(marco)

def preparaTabla( filas ):
    '''guarda la longitud mayor del dato'''
    longis = []
    for fila in filas:
        for e in fila:
            longis.append( len(e) )
        break
    for fila in filas:
        for i in range(len(fila)):
            if longis[i] < len(fila[i]):
                longis[i] = len(fila[i])
    return longis

    
main()
