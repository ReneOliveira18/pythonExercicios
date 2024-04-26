'''Faça um programa que leia um número qualquer e mostre
seu fatorial '''
# EX feito por mim
'''
print('=-='*7)
num = int(input('Digite um número para calcular seu fatorial: '))

cont = 1
result = 1
while cont <= num:
    result *= cont
    cont += 1
print('{}! = {}.'.format(num, result))
print('=-='*7)
'''
'''
#ex professor
n = int(input('Digite um número para calcular seu fatorial: '))

cont = n
result = 1
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')#aqui vai ter o if para aparecer o x e o = na tela do calculo de fatorial
    result *= cont
    cont -= 1
print('{}'.format(result))

'''

#outro metodo
from math import factorial

num = int(input('Digite um numero para calcular seu fatorial. '))
f = factorial(num)
print('O fatorial de {} = {}'.format(num, f))
