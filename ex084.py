'''
Leia nome e peso de várias pessoas, guardando tudo em uma lista. No
final mostre: a) quantas pessoas foram cadastradas. b) uma listagem
com as pessoas mais pesadas. c) uma listagem com as pessoas mais leves
'''
pessoas = list()
dado = list()
kgpesado = kgleve = c = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso em Kg: ')))
    pessoas.append(dado[:])
    dado.clear()
    sair = str(input('Deseja continuar? [S/N] ')).strip().lower()
    c += 1
    if sair == 'n':
        break

print(f'Nosso programa teve {c} pessoas cadastradas.')

for kg in pessoas:
    if kg[1] >= 90:
        print(f'O maior peso cadastrado foi de {kg[1]}kg. Peso de {kg[0]} ')
        kgpesado += 1

    if kg[1] <= 70:
        print(f'O menor peso cadastrado foi de {kg[1]}kg. Peso de {kg[0]}')
        kgleve += 1

print('---FIM---')
