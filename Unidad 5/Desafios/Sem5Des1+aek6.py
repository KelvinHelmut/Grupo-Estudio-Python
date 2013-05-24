#! /usr/bin/env python3.3
def main():
	print("Binario/Decimal")
	print("")
	while True:
		print("b. convertir a binario: ")
		print("d. convertir a decimal: ")
		print("s. salir")
		print("")
		op = input("Opcion: ")
		if op == 'b' or op == 'B':
			decimalABinario()
		elif op == 'd' or op == 'D':
			binarioADecimal()
		elif op == 's' or op == 'S':
			print("")
			print("Fin.")
			break
		else:
			print("Opcion invalida.")
			print("")
	
def decimalABinario():
	d = input("Dame un numero entero: ")
	while not esEntero(d):
		print(d,"No es un numero entero")
		d = input("Dame un numero entero: ")
	decimal = int(d)
	binario = "0"
	if decimal > 0:
		binario =" 1"
	while decimal > 1:
		binario += str( decimal % 2 )
		decimal = int( decimal / 2 )
	print("Resultado:",binario)
	print("")
	
def binarioADecimal():
	b = input("Dame un binario: ")
	while not esBinario(b):
		print(b,"No es un binario.")
		b = input("Dame un binario: ")
	t = len(b)
	decimal = 0
	for i in b:
		t -= 1
		decimal += ( int(i) * ( 2 ** t ) )
	print("Resulta:",decimal)
	print("")
	
	
def esEntero( numero ):
	for e in numero:
		if not esNumero(e):
			return False
	return True
	
def esNumero( e ):
	for n in ('0','1','2','3','4','5','6','7','8','9'):
		if e == n:
			return True
	return False
	
def esBinario( numero ):
	for n in numero:
		if not ( n == '0' or n == '1' ):
			return False
	return True
	
main()
