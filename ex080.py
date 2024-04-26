'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()). Nofinal mostre a lista ordenada em uma tela
'''
num = []
cont = 0
for cont in range(0,5):
    n = int(input('Digite um número: '))
    if cont == 0 or n > num[-1]: #para descobrir o primeiro e o ultimo elemento da lista
        num.append(n)
    else:
        posição = 0
        while posição < len(num):
            if n <= num[posição]:
                num.insert(posição, n)
                break
            posição += 1,                                                                                                                          ?N:
print('=-=' * 15)
print(f'Os valores são: {num}')