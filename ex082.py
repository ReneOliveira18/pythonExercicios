'''
Leia vários números e colocar em uma lista. Depois disso, crie duas
listas estras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre as 3 listas
'''
valores = []
pares = []
impares = []
print('=-=' * 15)
while True:
    valores.append(int(input('Digite um número. ')))
    sair = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if sair == 'n':
        break
print('=-=' * 15)
print(f'A lista é: {valores}')
for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('=-=' * 15)
print(f'Os valores pares desta lista são: {pares}')
print(f'Os valores ímpares desta lista são: {impares}')
print('=-=' * 15)