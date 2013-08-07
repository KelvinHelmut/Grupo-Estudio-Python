#! /usr/bin/python
# -*- coding: utf-8 -*-

class Caja(object):
    
    def __init__(self, nombre, dinero):
        if not self.esNumero(dinero):
            raise TypeError("dinero debe ser un valor numérico.")
        self.nombre = nombre
        self.dinero = dinero
        
    def esNumero(self, x):
        return isinstance(x, (int, float, complex))
        
    def desglosa(self, dinero):
        billetes = int(dinero / 10)
        mon25cen = int(round(dinero % 10, 2) / 0.25)
        mon10cen = int(round(round(dinero % 10, 2) % 0.25, 2) / 0.10)
        return billetes, mon25cen, mon10cen
        
    def __str__(self):
        dinero = self.desglosa(self.dinero)
        text = ('billetes de 10 pesos','monedas de 25 centavos','monedas de 10 centavos')
        texto = ''
        for i in range(0, len(dinero)):
            if dinero[i] == 0:
                continue
            else:
                if len(texto) > 0:
                    texto += ' y ' + str(dinero[i]) + ' ' + text[i]
                else:
                    texto += str(dinero[i]) + ' ' + text[i]
        return texto
    
    def __eq__(self, otro):
        return self.dinero == otro.dinero
                
    def __lt__(self, otro):
        return self.dinero < otro.dinero
    
    def __le__(self, otro):
        return self.dinero <= otro.dinero
        
    
    
c1 = Caja("caja1", 9.1)
c2 = Caja("caja2", 22.2)
c3 = Caja("caja3", 56)
c4 = Caja("caja4", 2)

print(c1 == c2)
print(c2 <= c1)

cs = [c1,c2,c3,c4]
cs.sort()
for e in cs:
    print(e)
