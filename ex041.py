from datetime import date

print('"-" ' * 7)
print('Somos a confederação de Natação Camaquense.')
datanasc = int(input('Vamos ver em que categoria você está.\n'
                     'digite seu ano de nascimento: '))
ano = date.today().year

cat = (ano - datanasc)

if cat <=9:
    print('Sua categoria é a Mirim, pois você tem {} anos.'.format(cat))

elif cat <= 14:
    print('Sua categoria é a Infantil, pois você tem {} anos. '.format(cat))

elif cat <= 19:
    print('Sua categoria é a Junior, pois você tem {} anos. '.format(cat))

elif cat <= 30:
    print('Sua categoria é a Adulta, pois você tem {} anos.'.format((cat)))

else:
    print('Sua categoria é a Master.')

print('Obrigado por usar nossa plataforma.')
print('"-" ' * 7)