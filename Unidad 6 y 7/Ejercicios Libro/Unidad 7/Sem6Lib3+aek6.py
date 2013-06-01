#!/usr/bin/env python3.3
import random

def poker( cartas ):
	''' retorna si las cartas ingresadas forman un
	poker( 4 de ellas son iguales) o no'''
	c = 0
	p = 0
	d = 0
	i = 1
	while i < 5:
		if cartas[p] == cartas[i]:
			c += 1
			p = i
		else:
			d += 1
			if d == 2 and p == 0:
				p += 1
				i = p
				d = 1
			elif d >= 2:
				break
		i += 1
	if c >= 3:
		return True
	return False
	
def main():
	baraja = ('A','1','2','3','4','5','6','7','8','9','10','J','Q','K')
	print( "Baraja: ", baraja )
	input("ENTER")
	while True:
		cartas = (random.choice( baraja ), random.choice( baraja ), random.choice( baraja ), random.choice( baraja ), random.choice( baraja ))
		print( "Cartas en juego: ", cartas )
		if poker(cartas):
			print("POKER!!")
			break
		else:
			print("...")
	#print( poker( ('4','4','4','2','4') ) )

main()
