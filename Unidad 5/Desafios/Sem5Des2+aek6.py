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
		
	print(fibo(0,1,limite))
		
def fibo( n1, n2, l ):
	if n2 <= l:
		return str(n1) + "\n" + fibo( n2, n1 + n2, l )
	return str( n1 )
	
main()
