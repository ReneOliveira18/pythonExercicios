#faça um programa que leia um número de 0 a
# 9999 e mostre na tela cada um dos digitos separedos
num = int(input('Entre com um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('unidade: {}\n'
      'dezena: {}\n'
      'centena: {}\n'
      'milhar: {}'.format(u, d, c, m))
