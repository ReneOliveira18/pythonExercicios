'''Leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequencia de Fibonacci'''
print('=--='*9)
print('Bem vindo a calculadora da Sequencia de Fibonacci. \n')

n = int(input('Número de termos que você deseja saber da sequencia de Fibonacci. '))
print('=--='*9)
primeirotermo = 0
segundotermo = 1

if (n == 1) or (n == 2):
    print('Número baixo de mais para fazer a sequencia de Fibonacci.')
else:
    print('{} {}'.format(primeirotermo, segundotermo), end='')
    cont = 3
    while cont <= n:
        termo = primeirotermo + segundotermo
        print(' {}'.format(termo), end='')
        primeirotermo = segundotermo
        segundotermo = termo
        cont += 1
print('')
print('--FIM--')
print('=--='*9)