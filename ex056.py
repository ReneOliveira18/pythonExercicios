#Leia o nome, idade e sexo de 4 pessoas, no final do programa mostre:
#a Media de idade, o nome do homem mais velho, quantas mulheres menores de 20 anos
soma = 0
media = 0
homemvelho = 0
nomevelho = ''
mulher20 = 0
for p in range(1,5):
    print('=== {}ª PESSOA ==='.format(p))
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo M (masculino) e F (feminino):')).strip().lower()
    idade = int(input('Idade: '))
    soma += idade
    if p == 1 and sexo == 'm':
        homemvelho = idade
        nomevelho = nome
    elif idade > homemvelho and sexo == 'm':
        homemvelho = idade
        nomevelho = nome
    elif idade < 20 and sexo == 'f':
        mulher20 += 1

media = (soma/4)
print('A média de idade é de {} anos.'.format(media))
print('O homem mais velho se chama {}.'.format(nomevelho))
print('Temos {} mulheres com menos de 20 anos.'.format(mulher20))