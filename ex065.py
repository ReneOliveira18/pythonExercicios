'''Leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar digitando
valores
'''
print('=-='*7)
print('Vamos calcular a média...')
print('=-='*7)
sair = ' '
cont = soma = media = maior = menor = 0
while sair != 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print('=-=' * 7)
    sair = str(input('S para Sair. ')).strip()[0].upper()
media = soma/cont
print('Calculamos {} nºs e sua média é {}'.format(cont, media))
print('O maior nº é {} e o menor nº é {}.'.format(maior, menor))
print('=-=' * 7)
print('--- FIM ---')
