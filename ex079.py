'''
Crie um programa onde o usuário possa digitar
vários valores númericos e cadastre-os en yna lista
Caso o número já exista lá dentro, ele não será adicionado
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
'''
print('=-=' * 13)
valores = list()
continuar = ''
while True:
    num = (int(input('Digite um valor: ')))
    print('=-=' * 13)
    if num not in valores:
        valores.append(num)
        print('Número adicionado com sucesso.')
    else:
        print('=-=' * 13)
        print('Número repetido, por favor adicionar outro número.')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        break
print('=-=' * 13)
print(f'O valores digitados são: {valores}')
print('=-=' * 13)
valores.sort()
print(f'Valores digitados em ordem crescente {valores}')
print('=-=' * 13)
print('===== FIM =====')