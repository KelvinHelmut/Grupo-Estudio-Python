#! /usr/bin/env python3.3
def main():
	limite = int(input("Digite la cantidad de numeros fibonacci que quiere: "))
	n = 0
	s = 1
	c = 0
	while c < limite:
		print(n)
		temp = s
		s = n + s
		n = temp
		c += 1
main()
