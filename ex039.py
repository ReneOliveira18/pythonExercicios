from datetime import date

print('~#~'*7)
print('Bem vindo ao exercito Brasileiro.')

sexo = str(input('Qual o seu sexo:\n'
                 'M - Masculino\n'
                 'F - Feminino\n'
                 'Sua opção: ')).upper()


if sexo == 'M':
    anonasc = int(input('Digite seu ano de nascimento: '))


    ano = date.today().year

    idade = (ano - anonasc)
    print(('Você tem {} anos'.format(idade)))
    if idade > 18:
        x = (idade - 18)
        alist = ano - x
        print('Faz {} anos que você se alistou.'.format(x))
        print('O ano do seu alistamento foi {}'.format(alist))
    elif idade < 18:
        x = (18 - idade)
        alist = ano + x
        print('Falta {} anos para você se alistar'.format(x))
        print('Você precisará se alista em {}'.format(alist))
    elif idade == 18:
        print(('Aliste-se já.Está no seu ano de alismetamento.'))
    else:
        print('Error')

elif sexo == 'F':
    print('Você é do sexo Feminino, não precisa se alistar.')

else:
    print('ERROR...')
print('Exercito Brasileiro a seu dispor.')
print('~#~'*7)
