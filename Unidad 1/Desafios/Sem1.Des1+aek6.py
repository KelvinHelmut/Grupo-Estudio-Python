def miEdad():
    anioActual = int( input("Año Actual:") )

    e1 = calculaEdad( anioActual )
    e2 = calculaEdad( anioActual )
    e3 = calculaEdad( anioActual )

    print(e1)
    print(e2)
    print(e3)

def calculaEdad( anio ):
    nombre = input("Dame tu nombre: ")
    anioNacimiento = int( input("Año de nacimiento: ") )

    mostrar = nombre , " este año cumples: " , anio - anioNacimiento , " año(s)"
    return mostrar


miEdad()
