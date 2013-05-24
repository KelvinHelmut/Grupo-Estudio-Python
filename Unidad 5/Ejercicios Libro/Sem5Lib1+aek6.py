#! /usr/bin/env python3.3

def cicloDefinido( tarifa ):
	cantidad = int(input("Cantidad de llamadas: "))
	while cantidad > 0:
		horas = int(input("Duracion de llamada - Horas: "))
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		cantidad -= 1
	
def cicloInteractivo( tarifa ):
	respuesta = "si"
	while respuesta == "si":
		horas = int(input("Duracion de llamada - Horas: "))
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		respuesta = input("¿Continuar ingresando llamadas [si/no]?: ")
		
def cicloCentinela( tarifa ):
	horas = int(input("Duracion de llamada - Horas [<0 para terminar]: "))
	while horas >= 0:
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		horas = int(input("Duracion de llamada - Horas [<0 para terminar]: "))
		
def cicloInfinito( tarifa ):
	while True:
		horas = int(input("Duracion de llamada - Horas [<0 para terminar]: "))
		if horas < 0:
			break
		minutos = int(input("Duracion de llamada - Minutos: "))
		segundos = int(input("Duracion de llamada - Segundos: "))
		duracion = obtenerSegundos( horas, minutos, segundos )
		costo = duracion * tarifa
		print("Duracion de llamada:",duracion,"segundos.")
		print("Costo de llamada:",costo)
		print("")
		
def obtenerSegundos( h, m, s ):
	return 3600 * h + 60 * m + s

def main():
	'''calcular costo de llamadas usando los bubles definido,interactivo
	centinela e infinito'''
	tarifa = float(input("Tarifa por segundo: "))
	cicloDefinido( tarifa )
	#cicloInteractivo( tarifa )
	#cicloCentinela( tarifa )
	#cicloInfinito( tarifa )

main()
