from math import p
'''
Leia um comprimento de 3 retas e diga se elas podem ou
não formar um triangulo
'''
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):#condição para as retas formarem triangulo
    print('\033[1:37:40mAs retas {}, {} e {} podem formar um triangulo.\033[m'.format(r1, r2, r3))

else:
    print('As retas {}, {} e {} NÃO podem formar um triangulo.'.format(r1, r2, r3))