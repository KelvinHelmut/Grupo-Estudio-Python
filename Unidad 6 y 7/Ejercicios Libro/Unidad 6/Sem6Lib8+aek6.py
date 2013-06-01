import random

digitos = ('0','1','2','3','4','5','6','7','8','9')

cant_digitos = 3
codigo = ''

for i in range( cant_digitos ):
    codigo += random.choice( digitos )
    
print("Bienvenido")
print("Tienes que adivinar un numero de", len(codigo),"cifras")
propuesta =  input("Que codigo propones?: ")

intentos = 1
while propuesta != codigo and propuesta != "Me doy":
	intentos += 1
	aciertos = 0
	coincidencias = 0
	codigoSinAciertos = ""
	propuestaSinAciertos = ""
	
	for i in range( len(codigo) ):
		if propuesta[i] == codigo[i]:
			aciertos += 1
		else:
			codigoSinAciertos += codigo[i]
			propuestaSinAciertos += propuesta[i]
		
	for i in range( len(codigoSinAciertos) ):
		if propuestaSinAciertos[i] in codigoSinAciertos:
			coincidencias += 1
			temp = codigoSinAciertos
			codigoSinAciertos = ""
			entro = False
			for j in range( len(temp) ):
				if temp[j] == propuestaSinAciertos[i] and not entro:
					entro = True
				else:
					codigoSinAciertos += temp[j]
					
	print("Tu propuesta (", propuesta, ") tiene", aciertos, "aciertos y", coincidencias, "coincidencias.")
	propuesta = input("Propone otro codigo: ")
	
if propuesta == "Me doy":
	print("El codigo era", codigo )
	print("Suerte la proxima vez!")
else:
	print("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
