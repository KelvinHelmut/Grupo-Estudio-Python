#! /usr/bin/env python3.3
def main():
	limite = int(input("Digite el numero limite de la susecion: "))
	n = 0
	s = 1
	while n <= limite:
		print(n)
		temp = s
		s = n + s
		n = temp
main()
