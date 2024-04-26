'''
Leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
o programa deverá perguntar se o usuário quer ou não continuar
no final mostre: a) quantas pessoas tem mais de 18 anos. b)
quantos homens foram cadastrados. c) quantas mulheres tem menos de
20 anos.
'''
'''
#meu desenvolvimento

print('=-=' * 7)
print('CADASTRO DE PESSOAS.')
print('=-=' * 7)
p = maior = masc = fem = 0
sair = sexo = ''
while True:
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual seu sexo Masculino e Feminino? [M/F]')).upper()[0].strip()
    print('=-=' * 7)
    p += 1
    if idade >= 18:
        maior += 1

    if sexo == 'M':
        masc += 1

    if sexo == 'F' and idade < 20:
        fem += 1

    sair = str(input('Digite S para sair: ')).upper()[0].strip()
    if sair == 'S':
        break
print(f'Cadastramos {p} pessoas em nosso programa \n'
      f'{maior} pessoas maiores de idade')
      f'{masc} são Homens \n'
      f'{fem} são mulheres com menos de 20 anos\n'

print('=-=' * 7)
print('---= FIM =---')
'''
#desenvolvimento guanabara
maior = masc = fem = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo Masculino ou Feminino [M/F] ')).strip().upper()[0]
        if idade >= 18:
            maior += 1

        if sexo == 'M':
            masc += 1

        if sexo == 'F' and idade < 20:
            fem += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{maior} pessoas maiores de 18 anos\n'
      f'{masc} pessoas do sexo masculino.\n'
      f'{fem} pessoas do sexo feminino com menos de 20 anos.')
print('---FIM---')