#! /usr/bin/env python3.3
def getCode():
	'''Pide codigo al usuario y lo devuelve
	en un diccionario'''
	code = {}
	n = 0
	tab = ''
	while True:
		n += 1
		code[n] = tab + input( str(n) + '\t'  + tab )
		if code[n].lower() == tab + 'exit':
			code.pop(n)
			break
		if code[n][-1] == ':':
			tab += '\t'
			continue
		tab = ''
	return code
	
def testCode( code ):
	'''verifica si tiene errores de identacion'''
	iden = 0 #identacion
	for i in code:
		'''if not( code[i][0] == '\t' or code[i][0] == ' ' ):
			iden = 0;'''
		for n in range(iden+1):
			if code[i][0 + n] == '\t':
				if n == iden:
					printError(i)
			elif code[i][0 + n] == ' ':
				printError(i)
			else:
				iden = n
				break
		'''if code[i][0 + iden] == '\t' or code[i][0 + iden] == ' ':
			print('error' + str(i) )'''
		if code[i][-1] == ':':
			iden += 1
			
def printError( linea ):
	'''imprime el mensaje de error de identacion'''
	print('Error!: En la linea', linea)
	
def main():
	testCode( getCode() )
	
main()
