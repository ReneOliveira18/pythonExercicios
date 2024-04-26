#Leia o ano de nascimento de sete pessoas. No final mostre
#quantas pessoas ainda não atingiram a maioridade e qtas são maiores
from datetime import date
print('=--='*9)

data = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    anonasci = int(input('Digite o ano do seu nascimento: \n'))
    idade = data - anonasci
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1

print('Temos {} pessoas maiores de idade e {} pessoas menores de idade.\n'.format(maior, menor))
print('---FIM---')
print('=--='*9)
