#!/usr/bin/python3.3

def agregarContacto():
    '''muestra mensaje de confirmacion y llama a la funcion agregar()'''
    print('')
    opcion = int( input( 'Agregar contacto [ si=1 / no=0 ]: ' ) )
    for i in range( 0, opcion ):
        opcion = 1

    return agregar( opcion )


def agregar( opcion ):
    '''agrega contacto y vuelve a llamar a la funcion agregarContacto()'''
    for i in range( 0, opcion ):
        return contacto() + agregarContacto()
    return('','')


def datos():
    '''pide datos al usuario y los devuelve en una tupla'''
    nombre = input( 'Dame tu nombre: ' )
    telefono = input( 'Dame tu telefono: ' )
    mail = input( 'Dame tu e-mail: ' )

    return( nombre, telefono, mail )


def contacto():
    '''retorna los datos del contacto'''
    return ( '', datos() )


#agregarContacto() devuleve los valores y lo guarda enpaquetados en contactos
contactos = agregarContacto()
print('')
print('Mi lista de contactos')
#print(contactos)
for contacto in contactos:
    print('--------------------------------------------------------')
    for datos in contacto:
        print( '>',datos )

