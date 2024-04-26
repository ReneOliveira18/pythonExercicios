'''Refaça o desafio 51 usando estrutura WHILE'''

print('=--='*9)
print('Bem vindo a calculadora de Progressão Aritimética\n')
print('=--='*9)

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

cont = 0
while cont <= 10:
    print('{} '.format(primeiro), end='')
    primeiro += razao
    cont += 1

print('')
print('--FIM--')
print('=--='*9)

