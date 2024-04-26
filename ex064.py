'''
Leia vários n inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada.
no final, mostre quantos n foram digitados e qual foi a soma
entre eles
'''
print('=-='*7)
print('Vamos SOMAR...')
print('=-='*7)
num = x = soma = 0
num = int(input('Digite um número [999 para parar]: ')) # vamos term o num aqui e na ultima linha do while para desconsiderar o 999 e ele não entrar no somatório
while num != 999:
    x += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('=-='*7)
print('O somatório de {} números é = {}'.format(x ,soma))
print('=-='*7)
print('---FIM---')