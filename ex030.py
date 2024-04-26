'''
Leia um numero inteiro e mostre na tela se
é par ou impar
'''

num = int(input('Digite um número, para analisar se é Par ou Ímpar: '))
par = num % 2

if par == 0:
    print('O numero {} é par.'.format(num))
else:
    print(('O numero {} é ímpar.'.format(num)))
