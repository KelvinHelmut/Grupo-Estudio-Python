#! /usr/bin/env python3.3

def cicloDefinido( tarifa ):
	cantidad = int(input("Cantidad de llamadas: "))
	i = 0
	total = 0
	while i < cantidad:
		horas = int(input("Duracion de llamada - Horas: "))
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		total += costo
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		i += 1
	return cantidad,total
	
def cicloInteractivo( tarifa ):
	respuesta = "si"
	c = 0
	total = 0
	while respuesta == "si":
		horas = int(input("Duracion de llamada - Horas: "))
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		c += 1
		total += costo
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		respuesta = input("¿Continuar ingresando llamadas [si/no]?: ")
	return c, total
		
def cicloCentinela( tarifa ):
	horas = int(input("Duracion de llamada - Horas [<0 para terminar]: "))
	c = 0
	total = 0
	while horas >= 0:
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		c += 1
		total += costo
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		horas = int(input("Duracion de llamada - Horas [<0 para terminar]: "))
	return c, total
		
def cicloInfinito( tarifa ):
	c = 0
	total = 0
	while True:
		horas = int(input("Duracion de llamada - Horas [<0 para terminar]: "))
		if horas < 0:
			return c, total
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		c += 1
		total += costo
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		
def obtenerSegundos( h, m, s ):
	return 3600 * h + 60 * m + s

def main():
	'''calcular costo de llamadas usando los bubles definido,interactivo
	centinela e infinito'''
	tarifa = float(input("Tarifa por segundo: "))
	#cantidad, total = cicloDefinido( tarifa )
	#cantidad, total = cicloInteractivo( tarifa )
	#cantidad, total = cicloCentinela( tarifa )
	cantidad, total = cicloInfinito( tarifa )
	print("Total de llamadas: ", cantidad )
	print("Total facturado: ", total )

main()
