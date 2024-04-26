'''
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla
'''
from random import sample

print('=-=' * 7)
print('VAMOS SORTEAR 5 NºS ALEATÓRIOS E DESCOBRIR MAIOR E O MENOR.')
print('=-=' * 7)
num = tuple(sample(range(11), 5)) #sample vai retornar uma nova lista de elementos RANGE(11), 5: loop de 0 até 10 que vai retornar 5 termos
print(f'Os nºs sorteados foram {num}\n'
      f'O maior valor foi {max(num)}\n'#max metodo específico das tuplas para achar o maior valor dentro da tupla
      f'O menor valor foi {min(num)}') #min igual o max só que para achar o menor valor
print('=-=' * 7)
print('--- F I M ---')
