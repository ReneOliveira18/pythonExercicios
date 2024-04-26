'''
Leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
Caso esteja errado, peça a digitação novamente até ter um valor
correto
'''
''' # Exercicio feito por mim 
while True:
    sexo = str(input('Qual seu sexo? [F/M] ')).upper()[0].strip()
    if sexo == 'M':
        print('Você é um Homem.')
        break
    elif sexo == 'F':
        print('Você é uma Mulher.')
        break
    else:
        print('Erro... digite M para masculino e F para feminino.')
print('--FIM--')
'''
#Corrigido pelo professor

sexo = str(input('Qual seu sexo? [F/M] ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Erro... digite M para masculino e F para feminino: ')).upper()[0].strip()
print('Sexo {} registrado.'.format(sexo))


