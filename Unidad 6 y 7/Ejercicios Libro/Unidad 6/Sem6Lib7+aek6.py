#! /usr/bin/python3.3
import random

digitos = ('0','1','2','3','4','5','6','7','8','9')

cant_digitos = 3
codigo = ''

for i in range( cant_digitos ):
    candidato = random.choice( digitos )
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

print(codigo)
print("Bienvenido")
print("Tienes que adivinar un numero de", len(codigo),"cifras distintas")
propuesta =  input("Que codigo propones?: ")

intentos = 1
while propuesta != codigo and propuesta != "Me doy":
    intentos += 1
    aciertos = 0
    coincidencias = 0

    for i in range( len(codigo) ):
        if propuesta[i] == codigo[i]:
            aciertos += 1
        elif propuesta[i] in codigo:
            coincidencias += 1

    print("Tu propuesta (", propuesta, ") tiene", aciertos, "aciertos y", coincidencias, "coincidencias.")
    propuesta = input("Propone otro codigo: ")

if propuesta == "Me doy":
    print("El codigo era", codigo )
    print("Suerte la proxima vez!")
else:
    print("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
