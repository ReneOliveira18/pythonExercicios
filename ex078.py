'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado
E suas respectivas posições na lista
'''

print('=-=' * 13)
valores = []
maior = 0
menor = 0
for cont in range (0, 5): #vai pedir para usuario digitar 5 valores
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('=-=' * 13)
print(f'Os valores digitados foram: {valores}')

print(f'O maior valor {max(valores)}, está na(s) posição(ões)', end=' ')
for indice, v in enumerate(valores):
    if v == maior:
        print(f'{indice}. ', end='')
print()
print(f'O menor valor {min(valores)}, está na(s) posição(ões)', end=' ')
for indice, v in enumerate(valores):
    if v == menor:
        print(f'{indice}. ', end='')
print()
print('=-=' * 13)
print('---FIM---')