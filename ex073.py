'''
Crie uma Tupla preenchida com os 20 primeiros colocados do Camp. Br
na ordem de colocação. Depois mostre:
a)Apenas os 5 primeiros colocados. b)os útimos 4 colocados.
c)Uma lista com os times em ordem alfabética. d)Em que posição
está o time da chapecoense.
'''
print('=-=' * 7)
print('BEM VINDO A TABELA DO BRASILEIRÃO.')
tabela = ('Internacional', 'Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Gremio', 'Fortaleza',
          'Chapecoense', 'Bahia', 'Bragantino', 'Atletico-MG', 'Botafogo', 'Criciúma', 'Cruzeiro', 'Cuiaba',
          'Juventude', 'São Paulo', 'Corinthians', 'Vitória', 'Vasco')
print('=-=' * 7)
#a)Apenas os 5 primeiros colocados.
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('=-=' * 7)
#b)os útimos 4 colocados.
print(f'Os 4 times rebaixados são: {tabela[16:20]}')# pode ser feito {tabela[-4:]} assim mostra os mesmos times
print('=-=' * 7)
#c)Uma lista com os times em ordem alfabética.
print(f'A ordem alfabética dos times é: \n'
      f'{sorted(tabela)}') #sorted vai recriar a tupla em ordem alfábetica
print('=-=' * 7)
print(f'A Chapecoense está na posição {tabela.index('Chapecoense')+1}')       #index vai localizar a palavra chapecoense e exibir qual sua posição na tupla. lembrando que a contagem começa do nº 0 zero
print('=-=' * 7)