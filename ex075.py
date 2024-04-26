'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final mostre: a) Quantas vezes apareceu o nº9
b)Em que posição foi digitado o primeiro nº 3 c) Qauis foram os nºs
pares
'''
print('=-=' * 7)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite mais um número: '))
tupla = (num1, num2, num3, num4)
print('=-=' * 7)
print(f'O valor 9 apareceu {tupla.count(9)} vezes') #resposta alternativa A
if 3 in tupla:
    print(f'O primeiro valor 3 digitado aparece na posição {tupla.index(3)+1}')  # resposta alternativa B
else:
    print('O valor 3 não foi encontrado.')
print('O valores pares são: ', end='')
for par in tupla:
    if par % 2 == 0:
        print(par, end=' ')
print('\n')
print('=-=' * 7)