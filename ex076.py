'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem
de preços, organizando os dados em forma tabular.
'''
from tabulate import tabulate

print('=-=' * 13)
lista = (['LISTA MERCADO', 'Valor(R$)'],
         ['Banana ', 4.99],
         ['Maça ', 3.88],
         ['Manga ', 6.55],
         ['Kiwi ',5.55],
         ['Tomate Cereja ', 5.99])
print(tabulate(lista, headers = 'firstrow', tablefmt='double_grid'))
print('=-=' * 13)

'''print('{:.<15} R${:.2f <10}'.format('Produto', 'Reais', 'Valor'))
produto = reais = valor = ' '
for mercado in lista:
    mercado = produto, reais, valor
    print('{:<15} {:<7} {:<15}'.format(produto, reais, valor))
'''
