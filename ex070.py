'''
Leia o nome e o preço de várior produtos o programa devera perguntar se o usuário vai continuar comprando
No final mostre:a) O total gasto na compra b) quantos produtos custaram mais de 1000 reais. c) O nome do
produto mais barato
'''
print('=-=' * 7)
print('BEM VINDO AO MERCADÃO ONLINE.')
print('=-=' * 7)
soma = contpreco = maisbarato = cont = 0
sair = nomebarato = nomeprod = ''
while True:
    nomeprod = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto:R$'))
    cont += 1
    soma += preco
    if preco >= 1000:
        contpreco += 1

    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        nomebarato = nomeprod

    sair = str(input('Digite S para Sair: ')).strip().upper()[0]
    if sair == 'S':
        break
print(f'O valor total gasto na compra foi de R${soma:.2f}\n'
      f'{contpreco} produtos custaram mais de R$1000.00 \n'
      f'O produto mais barato é {nomebarato} e custa R${maisbarato:.2f}')