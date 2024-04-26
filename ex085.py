'''
Crie um programa onde o usuário pode digitar 7 valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
'''
lista = []
c = cont = 0
pares = []
impares = []

for cont in range(0,7    lista.append(int(input(f'Digite {c+1}º número: ')))
    c += 1

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()
print(f'Os números pares digitados foram {pares}')
print(f'Os números ímpares digitados foram {impares}')