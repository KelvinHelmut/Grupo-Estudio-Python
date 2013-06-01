#! /usr/bin/env python3.3
def inscribir( ins ):
	padron = int( input('Ingresa un padron: ') )
	if padron <= 0:
		print('padron invalido!...\n')
		inscribir( ins )
		return 0
	if padron in ins:
		print('Ya figura en la lista')
		inscribir( ins )
		return 0
	ins.append( padron )
	
def borrar( ins ):
	print('Inscritos hasta ahora: ', ins )
	padron = int(input( 'ingrese el padron a remover: ' ))
	if padron in ins:
		ins.remove(padron)
	else:
		print('el padron ingresado no existe!')
	

def main():
	print( "Inscripcion en el curso 04 de 75.40")
	ins = []
	while True:
		print('1. Inscribir alumno')
		print('2. Borar alumno')
		print('3. Terminar')
		op = int( input('Eliga una opcion: ') )
		if op == 1:
			inscribir( ins )
		elif op == 2:
			borrar( ins )
		elif op == 3:
			break
		else:
			print('opcion invalida')
			continuar = input('ingrese (1) si quiere continuar: ')
			if continuar != '1':
				break
	print("Lista de inscritos: ", ins )

main()
