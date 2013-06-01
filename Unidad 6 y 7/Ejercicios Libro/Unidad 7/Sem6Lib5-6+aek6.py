#! /usr/bin/env python3.3

def diaSiguienteE( fecha ):
	'''devuelve la fecha del dia siguiente'''
	dia, mes, anio = fecha
	dia += 1
	if dia > diasMes( mes, anio ):
		dia = 1
		mes += 1
	if mes > 12:
		mes = 1
		anio += 1
	return dia, mes, anio
	
def diasMes( mes, anio ):
	'''retorna la cantidad maxima de dias del mes ingresado'''
	dias = ( 31, 28 + esBisiesto(anio), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 )
	return dias[mes - 1]

def nombreMes():
	return ( 'Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic' )
	
def esBisiesto( anio ):
	if anio%400 == 0:
		return 1
	elif anio%100 == 0:
		return 0
	elif anio%4 == 0:
		return 1
	return 0
	
def main():
	fecha = ( 28, 2, 2001 )
	print( diaSiguienteE( fecha ) )
	
	fecha = ( 28, 'Feb', 2000 )
	fecha = ( fecha[0], nombreMes().index( fecha[1] ) + 1, fecha[2] )
	fecha =  diaSiguienteE( fecha )
	print( fecha[0], nombreMes()[ fecha[1] - 1 ], fecha[2] )
	

main()
