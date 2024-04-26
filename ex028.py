'''
Escreva um programa que faça o computador *pensar*
em um numero inteiro entra 0 e 5 e peça para o
usuario tentar descobrir qual foi o número escolhido
pelo computador
O programa deverá escrever na tela se o usuario
ganhou ou perdeu
'''
from random import randint
from time import sleep
num = int(input('Digite um número entre 0 e 5: '))
print('Vamos ver se você acertou o numero que eu estava pensando...')
sorteio = randint(0,5)
sleep(1)
if num == sorteio:
    print('Uauuu, o número que pensei foi {} igual o seu.!'.format(sorteio))
else:
    print('Erroooooou, o numero que pensei foi {}.'.format(sorteio))

