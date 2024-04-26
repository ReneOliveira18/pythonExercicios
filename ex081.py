'''
Ler vários nºs e colocar em uma lista. a)quantos nºs foram digitados
b) ordem decrescente dos nºs e c) se o valor 5 foi digitado
'''
valor = []
num = 0
while True:
    num = int(input('Digite um nº: '))
    valor.append(num)
    sair = str(input('Deseja continuar? [S/N]')).strip().lower()
    if sair == 'n':
        break
print(f'Os nºs digitados foram: {valor})')
print(f'O tamanho da lista é de {len(valor)} números.')
valor.sort(reverse=True)
print(f'Sua ordem decrescente fica: {valor}')
if 5 in valor:
    print(f'O número 5 está na lista na posição {valor.index(5)} .')
elif 5 not in valor:
    print(f'O número 5 não foi digitado nesta lista.')