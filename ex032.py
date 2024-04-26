'''
Leia um ano qlqr e mostre se ele é Bissexto
'''
from datetime import date
ano = int(input('Digite o ano que você deseja saber se é Bissexto ou 0 para o ano atual: '))
#se (ano é multiplo de 4 e não multiplo de 100) ou (ser multiplo de 400) 'multiplo de 400 automaticamente é de 4'
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Este ano de {} é um ano Bissexto.'.format(ano))
else:
    print('Este ano de {} NÃO é Bissexto.'.format(ano))
