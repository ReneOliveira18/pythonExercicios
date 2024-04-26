'''Leia vários nºs inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos nºs foram digitados e qual
foi a soma entre eles. (desconsiderango a flag).'''
print('=-='*7)
print('Vamos calcular a Soma...\n'
      'Digite 999 para parar o somatório.')
print('=-='*7)
c = n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} nºs para calcular a soma e o seu resultado foi {s}')
print('=-=' * 7)
print('--- FIM ---')